import sys
import pandas as pd
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
import torch
import pickle
import nltk
nltk.download(['punkt','wordnet'])


def load_data(database_filepath):
    ''' load data from database and seperate the features and target column'''
    engine = create_engine('sqlite:///'+ database_filepath)
    df = pd.read_sql_table('messages',engine)
    X = df.message  #here message is the feature column
    y = df.iloc[:,4:]  # here column from 4  is the target column
    category_names = list(y.columns)
    return X, y, category_names


def tokenize(text):
    '''remove punctuation and tokenize the words'''
    text = re.sub(r'[^\w\s]','',text)
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    cln_tokens = []
    for i in tokens:
        tok = lemmatizer.lemmatize(i).lower().strip()
        cln_tokens.append(tok)
    return cln_tokens


def build_model():
    '''build the pipeline for the model and mention the grid search hyper params for finding bets params'''
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer(tokenizer=tokenize,max_df=0.75,ngram_range=(1,2))),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier(n_estimators=50)))
    ])

    parameters = {    
    'vectorizer__ngram_range': ((1, 1), (1, 2)),
    'vectorizer__max_df': (0.5, 0.75, 1.0),
    'clf__estimator__n_estimators': [50, 100, 200],
        
    }

    grid_cv = GridSearchCV(pipeline, param_grid=parameters, verbose=5, n_jobs=-1)

    return pipeline



def evaluate_model(model, X_test, Y_test, category_names):
    '''Returns the Classification report for the given model and test data'''
    y_pred = model.predict(X_test)
    for i, col in enumerate(category_names):
        print('{} category metrics: '.format(col))
        print(classification_report(Y_test.iloc[:,i], y_pred[:,i]))
          
def save_model(model, model_filepath):
    '''Saves the model to a pickle file'''
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)


        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
