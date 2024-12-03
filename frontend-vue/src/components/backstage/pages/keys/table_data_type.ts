interface KeyInfo {
  user_id?: string;
  user_name?: string;
  key: string;
  key_introduction: string;
  availableModels: string[];
  limit: number | null;
  residue_limit: number | null;
  enable?: boolean | null;
  charging?: boolean | null;
}
