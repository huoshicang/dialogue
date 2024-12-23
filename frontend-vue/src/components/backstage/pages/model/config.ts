export const columns = [
  {
    title: "创建人",
    dataIndex: "user_name",
    slotName: "user_name",
    width: 60,
    align: "center",
  },
  {
    title: "模型名",
    dataIndex: "model_name",
    ellipsis: true,
    tooltip: true,
    width: 90,
    align: "center",
  },
  {
    title: "调用名",
    dataIndex: "model_call",
    ellipsis: true,
    tooltip: true,
    width: 90,
    align: "center",
  },
  {
    title: "Base URL",
    dataIndex: "base_url",
    ellipsis: true,
    tooltip: true,
    width: 100,
    align: "center",
  },
  {
    title: "输入",
    dataIndex: "model_call_input",
    width: 50,
    align: "center",
  },
  {
    title: "输出",
    dataIndex: "model_call_output",
    width: 50,
    align: "center",
  },
  {
    title: "额度",
    slotName: "limit",
    width: 120,
    align: "center",
  },
  {
    title: "计费",
    slotName: "charging",
    width: 50,
    align: "center",
  },
  {
    title: "状态",
    slotName: "enable",
    width: 50,
    align: "center",
  },
  {
    title: "描述",
    dataIndex: "model_introduction",
    ellipsis: true,
    tooltip: true,
    width: 100,
    align: "center",
  },
  {
    title: "标签",
    slotName: "modelTag",
    align: "center",
    width: 110,
  },
  {
    title: "操作",
    slotName: "optional",
    width: 60,
    align: "center",
  },
];

export const modelTag = [
  '文本生成',
  "视频理解",
  "视频生成",
  "图片处理",
  "图片理解",
  "图片生成",
  "向量模型",
  "语音合成",
  "语音识别",
]

export const rules = {
  base_url: [
    {
      type: "url",
      required: true,
      message: "Base url 不可为空",
    },
  ],
  Model_name: [
    {
      required: true,
      message: "模型名 不可为空",
    },
  ],
  Model_call: [
    {
      required: true,
      message: "模型调用名 不可为空",
    },
  ],
  Model_introduction: [
    {
      required: false,
    },
  ],
  Model_call_input: [
    {
      required: true,
      message: "模型输入计费 不可为空",
    },
  ],
  Model_call_output: [
    {
      required: true,
      message: "模型输出计费 不可为空",
    },
  ],
  limit: [
    {
      required: true,
      message: "可用额度 不可为空",
    },
  ],
  residue_limit: [
    {
      required: true,
      message: "剩余额度 不可为空",
    },
  ],
};
