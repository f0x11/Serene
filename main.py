import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv

load_dotenv()  # 加载.env文件中的环境变量到os.environ
GLM_KEY = os.environ.get("GLM_KEY")
print(GLM_KEY)


def get_completions(tool, content):
    client = ZhipuAI(api_key=GLM_KEY)  # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4-flash",  # 请填写您要调用的模型名称
        messages=[
            {"role": "system", "content": """
            您是一个AI编程助手。
严格按照用户的字面要求执行。
您的回答应具有信息性和逻辑性。
始终遵循技术信息。
如果用户询问代码或技术问题，您必须提供代码建议并遵循技术信息。
如果问题与开发者相关，您必须以与开发者相关的内容进行回应。
首先逐步思考 - 详细写出构建计划的伪代码。
然后在单个代码块中输出代码。
尽量减少其他散文内容。
保持回答简短且客观。
在回答中输出可执行的python文件代码。
避免用三个引号包裹回答。
用户在JetBrains构建的IDE中工作，该IDE具有编辑器打开文件的概念、集成的单元测试支持以及显示代码运行输出的输出窗格以及集成的终端。
每次对话回合您只能给出一个回复。
"""},
            {"role": "user",
             "content": content},
        ],
    )
    res_text = response.choices[0].message.content.strip('```').strip('python')

    with open(tool, 'wb') as file:
        file.write(res_text.encode('utf-8'))


if __name__ == '__main__':
    get_completions('tool1.py', '帮我写一个工具，:v')
