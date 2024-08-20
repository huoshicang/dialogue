import requests
import time


def make_request(api_key, payload):
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/wordart/surnames"
    headers = {
        "X-DashScope-Async": "enable",
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"请求失败，状态码错误 {response.status_code}")


def check_task_status(api_key, task_id):
    url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"任务状态请求失败，状态码错误 {response.status_code}")


def main():
    api_key = 'sk-474a56d1d43140788d925a5888cda83a'

    payload = {
        "model": "wordart-surnames",
        "input": {
            "text": {
                "font_name": "gufeng1",
                "ttf_url": None,
                "text_strength": 0.5,
                "text_inverse": False
            },
            "surname": "冰",
            "style": "diy",
            "prompt": "女孩，花嫁",
            "ref_image_url": None
        },
        "parameters": {
            "n": 1
        }
    }

    # 发送请求并获取任务ID
    request_result = make_request(api_key, payload)
    task_id = request_result['output']['task_id']
    print(task_id)

    # 检查任务状态直到完成
    while True:
        task_status = check_task_status(api_key, task_id)['output']['task_status']
        if task_status == 'SUCCEEDED':
            results = check_task_status(api_key, task_id)['output']['results']
            print("任务已完成！")
            print("结果链接:", results[0]['url'])
            break
        elif task_status == 'FAILED':
            print("任务失败！")
            break
        else:
            print("任务仍在进行中...")
            time.sleep(5)  # 每隔5秒检查一次


if __name__ == "__main__":
    main()