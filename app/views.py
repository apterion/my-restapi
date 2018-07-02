from app import app
from app import db
from app import models
from flask import Response
from flask import jsonify
from flask import request as req
from flask import send_file
import datetime

@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])
def index():
    return send_file('static/index.html')

@app.route('/contracts', methods=['GET'])
def get_contracts():
    contracts = models.Contracts.query.all()
    data = {
        'contracts':[
            {
                'id': contract.id,
                'signed_date': contract.signed_date,
                'text': contract.text
            }
            for contract in contracts
        ]
    }
    return jsonify(data)

@app.route('/contracts/<int:contract_id>', methods=['GET'])
def get_contract_one(contract_id):
    contract = models.Contracts.query.filter_by(id=contract_id).first()
    if contract == None:
        return Response(status=404)
    else:
        data = {
            'id': contract.id,
            'signed_date': contract.signed_date,
            'text': contract.text
        }
        return jsonify(data)

@app.route('/contracts/<int:contract_id>', methods=['PUT'])
def update_contract(contract_id):
    data = req.get_json(force=True)
    contract = models.Contracts.query.filter_by(id=contract_id).first()
    if contract == None:
        return Response(status=404)
    else:
        contract.signed_date=datetime.datetime.strptime(data['signed_date'],'%Y-%m-%d')
        contract.text=data['text']
        contract.updated_date=datetime.date.today()
        db.session.commit()
        return str(contract_id);
    
@app.route('/contracts', methods=['POST'])
def add_contract():
    data = req.get_json(force=True)
    contract = models.Contracts(signed_date=datetime.datetime.strptime(data['signed_date'],'%Y-%m-%d'),
                                text=data['text'],
                                updated_date=datetime.date.today())
    db.session.add(contract)
    db.session.commit()
    return str(contract.id)
