def doc_to_text(doc) -> list:
    return f"""【重要格式要求】
必须使用LaTeX的\\boxed{{}}包裹最终答案
注意返回问题要求的答案格式
问题：{doc['problem']}

请分步骤思考后给出答案："""


    


