# uvicorn main:app --reload
import uvicorn

if __name__=="__main__":
    uvicorn.run("app.app:app",host='127.0.0.1', port=8000, root_path='/api', reload=True, workers=3)