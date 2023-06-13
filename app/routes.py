from app import app

from flask import render_template

@app.route('/')
def land():
     trails = [
        {
            'trail': 'Captian Ahab',
            'place': 'Moab,Utah'

        },
        {
            'trail': 'Chuckanut',
            'place': 'Bellingham,Washington'
        },
        {
            'trail': 'White Knuckle',
            'place': 'Port Angeles,Washington'
        },
        {
            'trail': 'Porcupine Rim Trail',
            'place': 'Moab,Utah'
        },
        {
            'trail': 'Mr. Toads',
            'place': 'South Lake Tahoe,California'
        }
            
    ]
        
        
     return render_template('index.html',trails=trails)
              
    
    


    

@app.route('/home')
def home():
       return 
        

@app.route('/test')
def test():
    return {
        'Is the mic on?': 'Is this function working??'
    }
