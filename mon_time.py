import requests
import time
from loguru import logger
import pymysql


class Equity:

    def __init__(self, phone):
        self.phone = phone
        logger.add(r'logfile.log')

    def connect_sql(self):
        self.conn = pymysql.connect(host="106.13.198.127", port=30399, user="metastudio", passwd="5edf4137f",
                                    db="meta_studio_test",
                                    charset="utf8")

    def execute_query(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        return data

    def get_token(self):
        sql1 = f"SELECT id from user WHERE phone='+86{self.phone}'"
        self.user_id = self.execute_query(sql1)[0][0]
        sql2 = f"SELECT access from oauth2_tokens WHERE user_id={self.user_id} AND delete_status=0"
        self.token = self.execute_query(sql2)[0][0]

    def mon(self):

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN",
            "Authorization": f"Bearer {self.token}",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Language-Error": "zh_CN",
            "OEM-From": "yuanLive",
            "Pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) yuan-live-test/1.9.0-beta.43 Chrome/110.0.5481.104 Electron/23.1.1 Safari/537.36",
            "X-Client-For": "1",
            "X-Target-For": "4"
        }
        url = f"http://api-ml.test.ex-ai.cn/v1/live/right/{self.user_id}"
        response = requests.get(url, headers=headers, verify=False)
        tmp = []
        for i in response.json()['data']:
            status = i.get('StopTimeDb').get('Valid')
            type_ = i.get('type')
            total = int(i['totalDuration'])
            used = int(i['usedDuration'])
            date = i['startTime']
            if status == False and (type_ in (3, 5, 6)):
                tmp.append((type_, date, total, used))

        sorted_tmp = sorted(tmp, key=lambda x: (x[0], x[1]))
        total = sorted_tmp[0][2]
        used = sorted_tmp[0][3]
        time = str((total - used) // 60) + 'min' + str((total - used) % 60) + 's'
        return time, used

    def run(self):
        self.connect_sql()
        while True:
            try:
                time.sleep(2)
                self.get_token()
                init_time, init_ = self.mon()
                new, _ = self.mon()
                if new != init_time:
                    logger.info(new)
                    if init_ - _ < 0:
                        t = (init_ - _) * -1
                        if t > 60:
                            time_ = str(t // 60) + 'min' + str(t % 60) + 's'
                            logger.info(f'消耗了{time_}')
                        else:
                            logger.info(f'消耗了{t}')
                    else:
                        t = init_ - _
                        if t > 60:
                            time_ = str(t // 60) + 'min' + str(t % 60) + 's'
                            logger.info(f'返还了{time_}')
                        else:
                            logger.info(f'返还了{t}')
                    init_time = new
                    init_ = _
                    logger.info('----------------')
            except Exception as e:
                print(e)
                logger.info('未知错误')

    def main(self):
        self.run()


phone = input('请输入手机号，如18500002001\n')
Equity(phone).main()
