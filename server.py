from flask import Flask, render_template

app = Flask(__name__)

# have the root route render a template with 8x8 checkerboard
@app.route('/')
def index():
    return render_template("index.html",row=8,column=8,color1='rebeccapurple',color2='peachpuff')

# have the another route accept a single parameter (x)
# render a checkerboard with x rows
@app.route('/<int:x>')
def difference_row(x):
    return render_template("index.html",row =x, column= 8, color1='rebeccapurple',color2='peachpuff')

# have another route accept 2 paramenters (x, y)
#  render a checkerboard with x rows, y coloumns
@app.route('/<int:x>/<int:y>')
def difference_row_and_column(x,y):
    return render_template("index.html",row =x, column= y, color1='rebeccapurple',color2='peachpuff')

# have another route accept 4 paramenters(x/y/<color1>/<color2>)
# render a checkerboard with x rows, y columns, with alternating colors, color1 and color2
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def freestyle(x,y,color1,color2):
    return render_template("index.html",row =x, column= y, color1=color1,color2=color2)

if __name__ == "__main__":
    app.run(debug = True)    
