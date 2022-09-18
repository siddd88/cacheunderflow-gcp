import flask,json
from flask import request, jsonify
from google.cloud import bigquery
import pandas as pd 
app = flask.Flask(__name__)

bigquery_client = bigquery.Client()

@app.route("/")

def main():
    post_id= request.args.get('post_id', default = '1', type = int)
    sql = """
        SELECT
        answer_count,comment_count
        FROM `bigquery-public-data.stackoverflow.stackoverflow_posts`
        where id={0}
    """.format(int(post_id))
    
    dataframe = ( bigquery_client.query(sql)
    .result()
    .to_dataframe(create_bqstorage_client=True,)
    )

    return {"data": json.loads(dataframe.to_json(orient='records'))}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)