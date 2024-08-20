export type RoleType = "" | "*" | "admin" | "user" | undefined;
export type NameType = "未登录" | string;
export interface UserState {
  name: NameType;
  avatar?: string;
  email?: string;
  introduction?: string;
  phone?: string;
  registrationDate?: string;
  accountId?: string;
  certification?: number;
  role: RoleType;
}
