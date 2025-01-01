// 定义正则表达式和 User-Agent 前缀
const urlRegex = /^http:\/\/.+\/amdc\/mobileDispatch/;
const userAgentPrefix = "AMapiPhone";
// 获取请求的 URL 和 User-Agent
const url = $request.url;
const userAgent = $request.headers["User-Agent"];
// 检查 URL 是否匹配正则表达式
const isUrlMatch = urlRegex.test(url);
// 检查 User-Agent 是否以指定前缀开头
const isUserAgentMatch = userAgent && userAgent.startsWith(userAgentPrefix);
// 如果两者都匹配，则返回 REJECT
if (isUrlMatch && isUserAgentMatch) {
  $done({ response: { status: 403, body: "Rejected by script" } });
} else {
  $done({});
}