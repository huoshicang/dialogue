export const columns = [
  {
    title: "创建人",
    dataIndex: "user_name",
    slotName: "user_name",
    width: 60,
    align: "center",
  },
  {
    title: "密钥",
    dataIndex: "key",
    ellipsis: true,
    tooltip: true,
    width: 90,
    align: "center",
  },
  {
    title: "额度",
    slotName: "limit",
    width: 120,
    align: "center",
  },
  {
    title: "可用模型",
    slotName: "availableModels",
    align: "center",
    width: 300,
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
    dataIndex: "key_introduction",
    ellipsis: true,
    tooltip: true,
    width: 100,
    align: "center",
  },
  {
    title: "操作",
    slotName: "optional",
    width: 60,
    align: "center",
  },
];

export const rules = {
  key: [
    {
      required: true,
      message: "密钥 不可为空",
    },
  ],
  key_introduction: [
    {
      required: false,
    },
  ],
  availableModels: [
    {
      required: false,
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
