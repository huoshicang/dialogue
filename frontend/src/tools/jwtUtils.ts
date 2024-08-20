import jwt from "jsonwebtoken";

interface Payload {
  [key: string]: any;
}

/**
 * 生成 JWT。
 * @param payload - 要包含在 JWT 中的有效载荷。
 * @param secret - 用于签名的密钥。
 * @param options - 可选的配置选项。
 * @returns 生成的 JWT 字符串。
 */
export const generate_jwt = (
  payload: Payload,
  secret: string,
  options?: jwt.SignOptions,
): string => {
  return jwt.sign(payload, secret, { algorithm: "HS256", ...options });
};

/**
 * 验证 JWT。
 * @param token - 要验证的 JWT 字符串。
 * @param secret - 用于验证的密钥。
 * @returns 解码后的有效载荷。
 */
export const verify_jwt = (token: string, secret: string): jwt.JwtPayload => {
  try {
    return jwt.verify(token, secret, {
      algorithms: ["HS256"],
    }) as jwt.JwtPayload;
  } catch (error) {
    console.error("Error verifying JWT:", error);
    throw error; // 你可以根据需要处理错误
  }
};
