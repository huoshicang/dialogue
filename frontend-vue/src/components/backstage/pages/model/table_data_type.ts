interface ModelInfo {
  user_id?: string;
  user_name?: string;
  base_url: string;
  model_name: string;
  model_call: string;
  model_introduction: string;
  model_call_input: number | null;
  model_call_output: number | null;
  limit: number | null;
  residue_limit: number | null;
  enable?: boolean | null;
  charging?: boolean | null;
}

interface ModelInfoForm {
  base_url: string;
  Model_name: string;
  Model_call: string;
  Model_introduction: string;
  Model_tag: [],
  Model_call_input: number | null;
  Model_call_output: number | null;
  limit: number | null;
  residue_limit: number | null;
  enable?: boolean;
  charging?: boolean;
}
