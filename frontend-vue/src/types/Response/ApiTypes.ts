export interface get_chat_list_type {
  user_id: string;
}

export interface ChatParameters {
  model: string;
  messages: any[]; // 假设消息是任意类型的数组，你可以根据实际情况调整类型
  top_p: number;
  temperature: number;
  presence_penalty?: number | null; // 使用可选属性和联合类型来表示可能的null值
  max_tokens?: number | null;
  response_format: "text"; // 如果响应格式固定为"text"，可以使用字面量类型
  seed?: number | null;
  stream: boolean;
  stop?: string | null | string[]; // 如果stop可以是一个字符串、字符串数组或null
  tools?: any[] | null; // 工具的类型取决于具体需求，这里假设它们可能是任意类型的数组或null
  stream_options?: any | null; // 流选项的类型取决于具体需求
  enable_search: boolean;
}

export interface add_chat_type {
  user_id: string; // 或者其他适合user_info._id的类型
  user_name: string;
  chat_title: string;
  system: string;
  chat_parameters: ChatParameters;
}

export interface get_model_table_type {
  user_id: string;
  user_name: string;
  user_role: string;
}
