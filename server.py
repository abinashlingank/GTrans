from flask import Flask, request, jsonify
from trans import translate_to_english
from trans import translate_to_tamil
app = Flask(__name__)

@app.route('/forward', methods=['POST'])
def translate():
    data = request.json  # Assuming data is sent as JSON
    # Perform processing on the data
    startlan=data["source"]
    text=data["text"]
    translated=translate_to_english(text,startlan)
    return jsonify({"text":translated,"source":data["source"],"dest":data["dest"]})

@app.route('/backward',methods=['POST'])
def backward():
    data=request.json
    backlan=data["dest"]
    text=data["text"]
    translated=translate_to_tamil(text,backlan)
    return jsonify({"text":translated,"source":data["source"],"dest":data["dest"]})


'''
return=>{response text,links of buses,buttonstat,button text}
'''
if __name__ == '__main__':
    app.run(debug=True,port=5000)
