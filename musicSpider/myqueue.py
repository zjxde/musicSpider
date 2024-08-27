import abc
import concurrent.futures
import queue
import threading


class AbstractBatchQueue(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handleTask(self, data):
        pass

    def __init__(self):
        # 创建队列
        self.q = queue.Queue()
        print("==========")

    def batchPut(self, data, batch_size=1):
        # 添加一些数据到队列中
        for i in range(batch_size):
            self.q.put(data)

    def batchGet(self, batch_size):
        q = self.q
        # 批量取出队列中的数据
        # 假设我们想要一次取出5个元素
        batch = []

        # 循环直到队列为空
        while not q.empty():
            # 尝试获取batch_size个元素
            for _ in range(batch_size):
                # 尝试从队列中取出元素，如果队列为空，会抛出异常
                try:
                    item = q.get_nowait()
                    batch.append(item)
                except queue.Empty:
                    # 队列为空时，退出循环
                    break
            # 处理批量获取的元素
            self.handleTask(batch)
            batch = []  # 重置批处理列表

        # 如果队列中剩余元素少于batch_size，在循环结束后处理剩余元素
        if batch:
            self.handleTask(batch)


class BatchQueue(AbstractBatchQueue):

    def __init__(self):
        super().__init__()
        thread = threading.Thread(target=self.comsum)
        thread.start()

    def handleTask(self, data_list):
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # 提交任务到线程池中
            executor.submit(self.save_data, data_list)

    def save_data(self, data_list):
        print(data_list)

    def comsum(self):
        while True:
            self.batchGet(2)
            # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            #     executor.submit(self.batchGet, 2)
            # print("=================")


if __name__ == '__main__':
    batch_queue = BatchQueue()
    batch_queue.batchPut("aa", 100)
    batch_queue.batchGet(9)

    batch_queue2 = BatchQueue()
    batch_queue2.batchPut("bb", 100)
    batch_queue2.batchGet(9)
