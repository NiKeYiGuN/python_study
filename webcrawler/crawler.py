# type: ignore
import csv
import os
import requests
import pandas as pd

url = "https://m.maoyan.com/mmdb/comments/movie/257706.json?v=yes&offset=30"

payload = {}
headers = {
    "Cookie": "_lxsdk_cuid=17c188b300d13-0ecb2e1c54bec6-a7d173c-100200-17c188b300ec8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1633622378; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=87266087.1633622378325.1633622378325.1633622378325.1; uuid_n_v=v1; iuuid=ECBA18D0278711EC8B0DFD12EB2962D2C4A641A554EF466B9362A58679FDD6CF; webp=true; ci=55%2C%E5%8D%97%E4%BA%AC; ci=55%2C%E5%8D%97%E4%BA%AC; ci=55%2C%E5%8D%97%E4%BA%AC; featrues=[object Object]; _lxsdk=92E6A4E0278711ECAE4571A477FD49B513FE367C52044EB5A6974451969DD28A; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1633622806",
    "Host": "m.maoyan.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())


def save_data_pd(data_name, list_info):
    if not os.path.exists(data_name + r"_data.csv"):
        # 表头
        name = [
            "comment_id",
            "approve",
            "reply",
            "comment_time",
            "sureViewed",
            "nickName",
            "gender",
            "cityName",
            "userLevel",
            "user_id",
            "score",
            "content",
        ]
        # 建立DataFrame对象
        file_test = pd.DataFrame(columns=name, data=list_info)
        # 数据写入
        file_test.to_csv(data_name + r"_data.csv", encoding="utf-8", index=False)
    else:
        with open(
            data_name + r"_data.csv", "a+", newline="", encoding="utf-8"
        ) as file_test:
            # 追加到文件后面
            writer = csv.writer(file_test)
            # 写入文件
            writer.writerows(list_info)
