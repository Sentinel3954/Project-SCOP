from web3 import Web3
from web3.middleware import geth_poa_middleware
import logging
from threading import Thread

class WatchMiner():
    def __init__(self, threads: int = 1, provider: str | None = 'http://127.0.0.1:8545'):
        self.threads = threads
        self.provider = provider
        self.w3 = None
        self.block = None
        self.mine_thread = None
        self.mining = False
        self.working = False
        self.logger = logging.getLogger(__name__)

    def connect(self):
        self.w3 = Web3(Web3.HTTPProvider(self.provider))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)                                                        # allow more that 32bits in data
        self.w3.geth.miner.set_gas_price('0x0')                                                                              # transactions a FREE now
        try:
            self.w3.geth.miner.start_auto_dag()                                                                              # enable auto DAG generetion (to prevent a massive block delay on each epoch transition)
        except: pass
        self.blockNumber = self.w3.eth.blockNumber
        self.logger.info('WhatchMiner connected to provider')

    def check_new_block(self) -> int:
        if not self.w3: self.connect()
        self.block = self.w3.eth.get_block('pending')
        if self.w3.eth.blockNumber != self.blockNumber:
            self.blockNumber = self.w3.eth.blockNumber
            self.logger.debug(f'Commited {self.blockNumber} block')
        return self.blockNumber

    def run_miner(self) -> bool:
        if not self.w3: self.connect()
        if not self.mining:
            self.w3.geth.miner.start(self.threads)
            self.mining = True
            self.logger.info('Miner started')
            return True
        return False

    def stop_miner(self) -> bool:
        if self.mining:
            self.w3.geth.miner.stop()
            self.mining = False
            self.logger.info('Miner stoped')
            return True
        return False

    def watch(self):
        try:
            while self.working:
                self.check_new_block()
                if len(self.block['transactions']) > 0:
                    self.run_miner()
                else:
                    self.stop_miner()
        except Exception as e:
            self.logger.critical(f'WhatchMiner stoped for the reason: {e}')
        
    def start(self) -> bool:
        if not self.working:
            self.working = True
            self.mine_thread = Thread(target = self.watch)
            self.mine_thread.daemon = True
            self.mine_thread.start()
            self.logger.info('WhatchMiner started')
        return True

    def stop(self) -> bool:
        if self.working:
            self.working = False
            self.mine_thread.join()
            self.logger.info('WhatchMiner stoped')
        return True

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s %(message)s')
    miner = WatchMiner(threads=2)
    miner.connect()

    # CLI App
    miner.logger.info('Running in CLI mode...')
    COMMANDS = [
        'help           - list of commands',
        'blockNumber    - last checked block number',
        'start          - start WatchMiner instance',
        'stop           - stop WatchMiner instance',
        'minerStart     - start miner (UNCONTROLLED mining, DONT USE IT)',
        'minerStop      - stop miner immideatly (can be ignored by WatchMiner)',
        'isWorking      - check is WatchMiner started',
        'isMining       - check miner started',
        'exit           - stop application',
    ]
    help = '\n'.join(COMMANDS)
    while (command:= input('> ')) != 'exit':
        if command == 'help':
            print(help)
        elif command == 'blockNumber':
            miner.check_new_block()
            print(miner.blockNumber)
        elif command == 'start':
            miner.start()
        elif command == 'stop':
            miner.stop()
        elif command == 'minerStart':
            agreement = input('Are you sure? y/n')
            if agreement.upper() == 'Y':
                miner.run_miner()
            else:
                print('Miner not started')
        elif command == 'minerStop':
            miner.stop_miner()
        elif command == 'isWorking':
            print(miner.working)
        elif command == 'isMining':
            print(miner.mining)
        else:
            print('Print "help" to get list of commands')
    miner.stop()