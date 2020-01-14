import flask
import pandas as pd
from flask_cors import CORS
from flask import request
from statistics import *

def create_app():
    app = flask.Flask(__name__)
    CORS(app)


    @app.route('/', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    @app.route('/sensors', methods=['GET', 'POST'])
    @app.route('/samples', methods=['GET', 'POST'])
    @app.route('/sensors/compare', methods=['GET', 'POST'])
    @app.route('/samples/compare', methods=['GET', 'POST'])
    @app.route('/layout', methods=['GET', 'POST'])
    @app.route('/all', methods=['GET', 'POST'])
    def index():
        """
        Index page view handler.
        :return: rendered index.html template
        """
        return flask.render_template('index.html')

    @app.route('/sample/<path:sampleId>', methods=['GET', 'POST'])
    def sampleIdRoute(sampleId):
        return flask.render_template('index.html')


    @app.route('/homeStat', methods=['GET', 'POST'])
    def homeStat():
        data = pd.read_csv('task_data.csv')
        result = data['class_label'].tolist()
        unique_list = []
        sensors = [col for col in data.columns if 'sensor' in col]

        for x in result: 
            if x not in unique_list: 
                unique_list.append(x) 

        positives = len(data.loc[data['class_label'] == 1].index)
        negatives =  len(data.loc[data['class_label'] == -1].index)

        result = {
            'positives': positives,
            'negatives': negatives,
            'classTypeCount': unique_list,
            'sensors': sensors,
        }

        return flask.jsonify(result)

    @app.route('/sensorsmedian', methods=['GET', 'POST'])
    def sensorsmedian():
        data = pd.read_csv('task_data.csv')
        data.columns = data.columns.str.replace(' ', '_')
        meds = []
        sensors =  [2,3,4,5,6,7,8,9,10,11]

        for s in sensors:
            sensorMed = median(list(data[data.columns[s]]))
            meds.append(sensorMed)

        return flask.jsonify(meds)


    @app.route('/sampleData', methods=['GET', 'POST'])
    def sampleData():
        data = pd.read_csv('task_data.csv')
        data.columns = data.columns.str.replace(' ', '_')
        sample = request.args.get('sample')
               
        sampleData = list(data.loc[data['sample_index'] == sample].apply(lambda x: x.to_dict(), axis=1))

        return flask.jsonify(sampleData)

    @app.route('/stat', methods=['GET', 'POST'])
    def stat():
        data = pd.read_csv('task_data.csv')
        sensor = request.args.get('sensor')

        context ={
            'min':data[sensor].min(axis = 0),
            'max':data[sensor].max(axis = 0),
            'median':data[sensor].median(axis = 0),
            'upperq':data[sensor].quantile(0.75),
            'lowerq':data[sensor].quantile(0.25)
        }

        return flask.jsonify(context)

    @app.route('/parallelcood', methods=['GET', 'POST'])
    def parallelCood():
        data = pd.read_csv('task_data.csv')
        columns = list(data.columns.values)

        con = {
            'columns': columns,
            'result':data.as_matrix().tolist()
        }

        return flask.jsonify(con)
        

    @app.route('/pareto', methods=['GET', 'POST'])
    def sensordistribution():
        quartiles =  [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
        sensor = request.args.get('sensor')
        data = pd.read_csv('task_data.csv')
        pareto = []
        
        for q in quartiles:
            pareto.append(data[sensor].quantile(q))

        context ={
            'pareto': pareto,
            'quartiles': quartiles
        }
        return flask.jsonify(context)

    @app.route('/latest', methods=['GET', 'POST'])
    def sensor():
        data = pd.read_csv('task_data.csv')
        data.columns = data.columns.str.replace(' ', '_')

        sensors = [col for col in data.columns if 'sensor' in col]
        latest = data.loc[data.index[-1]]

        context = {
            'sensors':sensors,
            'latest': latest.to_dict(),
        }
        return flask.jsonify(context)

    @app.route('/data', methods=['GET', 'POST'])
    def data():
        """
        Data view handler
        :return: JSON object of the data CSV file
        """
        data = pd.read_csv('task_data.csv')
        data.columns = data.columns.str.replace(' ', '_')

        total = data.apply(lambda x : x.last_valid_index()).add(1).to_dict()
        

        positives = data.loc[data['class_label'] == 1]
        negatives =  data.loc[data['class_label'] == -1]

        pMinData = positives.min(axis = 0).to_dict()
        pMaxData = positives.max(axis = 0).to_dict()
        pMedianData = positives.median(axis = 0).to_dict()
        pUpperQuad = positives.quantile(0.75).to_dict()
        pLowerQuad = positives.quantile(0.25).to_dict()


        
        nMinData = negatives.min(axis = 0).to_dict()
        nMaxData = negatives.max(axis = 0).to_dict()
        nMedianData = negatives.median(axis = 0).to_dict()
        nUpperQuad = negatives.quantile(0.75).to_dict()
        nLowerQuad = negatives.quantile(0.25).to_dict()



        sensors = [col for col in data.columns if 'sensor' in col]
        samples  = data['sample_index'].tolist()

        context = {
            'sensor_data': data.to_dict(orient='list'),
            'total': total,
            'all': data.apply(lambda x: x.to_dict(), axis=1).to_dict(),
            'positives': positives.apply(lambda x: x.to_dict(), axis=1).to_dict(),
            'negatives': negatives.apply(lambda x: x.to_dict(), axis=1).to_dict(),
            'sensors':sensors,
            'samples': samples,
            'box':
                {'positives':{'min': pMinData, 'lowerQuad':pLowerQuad, 'median':pMedianData ,'upperQuad':pUpperQuad, 'max': pMaxData},
                 'negatives':{'min': nMinData,'lowerQuad':nLowerQuad,  'median':nMedianData , 'upperQuad':nUpperQuad,'max': nMaxData}
                },
        }
        return flask.jsonify(context)

    return app


if __name__ == "__main__":
    app = create_app()
    # serve the application on port 7410
    app.run(host='0.0.0.0', port=7410)
