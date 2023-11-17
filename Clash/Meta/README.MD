# ClashVerge


下载Clash.Meta内核客户端
---
- [Clash Verge 下载地址](https://github.com/zzzgydi/clash-verge)


本地配置（推荐）
---
> 以处`Clash Verge`为例
#### 0.设置内核为 `Clash.Meta`
![0](https://github.com/Repcz/Tool/blob/X/Clash/Meta/Photo/0.png)
#### 1.下载配置文件`ClashVerge.yaml`文件到本地

<details>
  <summary>ClashVerge.yaml</summary>

- [x] 地区分流（香港、美国、日本、台湾、新加坡、澳大利亚、英国、印度）
- [x] 苹果、谷歌、微软、电报、推特分流
- [x] 流媒体（不支持单独分流）
- [x] 自动选择最低延迟
- [ ] 负载均衡
- [ ] 故障转移
- [x] 广告屏蔽

</details>

```
https://raw.githubusercontent.com/Repcz/Tool/X/Clash/Meta/ClashVerge.yaml
```

#### 2. 修改配置 `proxy-providers` 中的机场订阅地址
* 请自行将 `proxy-providers` 中的 `机场订阅` 替换为机场订阅地址

```yaml
proxy-providers:
  Subscribe: {<<: *p, path: ./all.yaml, url: 机场订阅}
    # Meta支持机场通用订阅
```


#### 3. Clash Verge 中导入 **配置**
* 打开Clash Verge，点击 **配置**，点击右下角**新建**
* 类型选择**Local**，点击下方 **选择文件**，选择修改好的文件
* 点击 **代理** ，设置分流


#### 4. 启用配置
* 选择导入的配置，右键-启用



策略组修改为手动选择节点
---
> 默认为自动选择延迟最低节点，**按需** 修改为手动选择
* 在自定义策略下的分流策略组中选择需要的地区节点，此处以 **国外网站** 举例，选择 **香港节点**
* 下拉到下方的 **香港节点** 策略组，此时该策略组以 `url-test` 运行，即按最低延迟选择节点
* 如果要修改为手动选择节点，则需要编辑配置文件，在 **配置** ，右键需要修改的配置文件，点击 **编辑**
* 找到` - {name: 🇭🇰 香港节点, <<: *auto, filter: "港|HK|(?i)Hong"}`，将 `*auto` 修改为 `*use`
* 在 **香港节点** 策略组中选择需要的节点，则 **国外网站** 策略组走 **香港节点** 中选择的节点

eg:
```yaml
...

 - {name: 🇭🇰 香港节点, <<: *auto, filter: "港|HK|(?i)Hong"}

👇

 - {name: 🇭🇰 香港节点, <<: *use, filter: "港|HK|(?i)Hong"}

...

```

订阅转换（懒人方法）
---
### 在线订阅转换
> 在线订阅转换可能出现订阅泄露
#### 1. 打开[ACL4SSR](https://acl4ssr-sub.github.io/) 
#### 2. 填入 **机场订阅** 和 **远程配置**

**_自用 多流媒体分组 自动测速 配置_**
```
https://raw.githubusercontent.com/Repcz/Tool/X/Clash/Meta/Online_Full_Auto.ini
```
#### 3. 选择后端地址并生成订阅
* 强烈建议使用自建后端，自建后端订阅转换可以有效防止订阅泄露以及规则下载不全等问题，具体方法见[自建subconverter订阅转换](https://github.com/Repcz/Tool/X/subconverter)

![4](https://github.com/Repcz/Tool/blob/X/Clash/Meta/Photo/4.PNG)

### 本地后端订阅转换（推荐）
详细使用方法见[自建subconverter订阅转换](https://github.com/Repcz/Tool/X/subconverter)


### 导入Clash Verge
* 打开Clash Verge，点击 **配置**，导入**订阅转换**后的链接
* 点击 **代理** ，设置分流