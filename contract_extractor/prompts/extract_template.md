# 依頼内容

以下の3点の回答条件を踏まえて、下方に定義するJSONを返答してください。

## 回答条件

1. 以下の文脈を踏まえて回答すること
2. 可能な限り文脈に含まれる単語だけで回答を作成すること
3. 必ずJSONフォーマットでの回答を返すこと
4. 抽出できなかった項目についてはnullで返すこと
5. 日付が入る項目については必ずYYYY-MM-DDの形式で返すこと

## 文脈

{context}

## 出力形式

JSONフォーマットで回答してください。
以下のようなJSONのフォーマットにて回答を作成してください。

```json
{{
    "document_title": "業務委託契約書",
    "companies": [
        {{
            "name": "A株式会社",
            "role": "customer",
            "address": {{
                "prefecture": "愛知県",
                "city": "岡崎市",
                "town": "十王町",
                "street": "2-9",
            }}
        }},
        {{
            "name": "B株式会社",
            "role": "provider",
            "address": {{
                "prefecture": "愛知県",
                "city": "西尾市",
                "town": "寄住町下田",
                "street": "22"
            }}
        }},
    ],
    "contract_term": {{
        "start_date": "2024-04-01",
        "end_date": "2030-12-31"
    }},
}}
```

回答をお願いいたします。
