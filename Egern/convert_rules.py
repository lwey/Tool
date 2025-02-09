import re
import sys
from pathlib import Path
# 定义 Surge 规则到 egern 规则的映射
RULE_MAPPING = {
    "DOMAIN": "domain",
    "DOMAIN-SUFFIX": "domain_suffix",
    "DOMAIN-KEYWORD": "domain_keyword",
    "DOMAIN-WILDCARD": "domain_wildcard",
    "IP-CIDR": "ip_cidr",
    "IP-CIDR6": "ip_cidr6",
    "IP-ASN": "asn",
    "URL-REGEX": "url_regex",
    "DEST-PORT": "dest_port",
    "GEOIP": "geoip",
}
# 定义逻辑规则的正则表达式
LOGIC_RULE_REGEX = re.compile(r"^(AND|OR|NOT),\(\((.*)\), \((.*)\)\)$")
def parse_logic_rule(rule):
    """
    解析逻辑规则（AND, OR, NOT）并转换为 egern 格式。
    """
    match = LOGIC_RULE_REGEX.match(rule)
    if not match:
        return None
    logic_type = match.group(1).lower()  # AND -> and, OR -> or, NOT -> not
    rule1 = parse_single_rule(match.group(2))
    rule2 = parse_single_rule(match.group(3))
    if not rule1 or not rule2:
        return None
    return {
        logic_type: {
            "match": [rule1, rule2]
        }
    }
def parse_single_rule(rule):
    """
    解析单条规则（如 DOMAIN, DOMAIN-SUFFIX 等）并转换为 egern 格式。
    """
    parts = rule.split(",")
    if len(parts) < 2:
        return None
    rule_type = parts[0]
    rule_value = parts[1]
    if rule_type not in RULE_MAPPING:
        return None
    return {
        RULE_MAPPING[rule_type]: rule_value
    }
def convert_file(file_path):
    """
    转换单个文件中的规则。
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    output_lines = []
    domain_set_added = False
    domain_suffix_set_added = False
    domain_keyword_set_added = False
    domain_wildcard_set_added = False
    ip_cidr_set_added = False
    ip_cidr6_set_added = False
    asn_set_added = False
    url_regex_set_added = False
    dest_port_set_added = False
    geoip_set_added = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # 删除不需要的规则
        if line.startswith(("USER-AGENT", "PROCESS-NAME")):
            continue
        # 解析逻辑规则
        logic_rule = parse_logic_rule(line)
        if logic_rule:
            output_lines.append(str(logic_rule))  # 将字典转换为字符串
            continue
        # 解析单条规则
        single_rule = parse_single_rule(line)
        if single_rule:
            rule_type = list(single_rule.keys())[0]
            rule_value = single_rule[rule_type]
            # 添加集合头（如 domain_set:）
            if rule_type == "domain" and not domain_set_added:
                output_lines.append("domain_set:")
                domain_set_added = True
            elif rule_type == "domain_suffix" and not domain_suffix_set_added:
                output_lines.append("domain_suffix_set:")
                domain_suffix_set_added = True
            elif rule_type == "domain_keyword" and not domain_keyword_set_added:
                output_lines.append("domain_keyword_set:")
                domain_keyword_set_added = True
            elif rule_type == "domain_wildcard" and not domain_wildcard_set_added:
                output_lines.append("domain_wildcard_set:")
                domain_wildcard_set_added = True
            elif rule_type == "ip_cidr" and not ip_cidr_set_added:
                output_lines.append("ip_cidr_set:")
                ip_cidr_set_added = True
            elif rule_type == "ip_cidr6" and not ip_cidr6_set_added:
                output_lines.append("ip_cidr6_set:")
                ip_cidr6_set_added = True
            elif rule_type == "asn" and not asn_set_added:
                output_lines.append("asn_set:")
                asn_set_added = True
            elif rule_type == "url_regex" and not url_regex_set_added:
                output_lines.append("url_regex_set:")
                url_regex_set_added = True
            elif rule_type == "dest_port" and not dest_port_set_added:
                output_lines.append("dest_port_set:")
                dest_port_set_added = True
            elif rule_type == "geoip" and not geoip_set_added:
                output_lines.append("geoip_set:")
                geoip_set_added = True
            # 添加规则
            output_lines.append(f"  - {rule_value}")
    # 写入转换后的内容
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(output_lines))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_rules.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    convert_file(file_path)