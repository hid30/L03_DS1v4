import pandas as pd
import pickle

# Load model
with open(r'C:\Users\LENOVO\Proyek Data Science 1\best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Data baru untuk prediksi
df_new = pd.DataFrame({ 
    'Age': [35],
    'DailyRate': [555],
    'DistanceFromHome': [1],
    'HourlyRate':[77],
    'MonthlyRate':[13500],
    'NumCompaniesWorked':[2],
    'PercentSalaryHike':[10],
    'TrainingTimesLastYear':[3],
    'YearsAtCompany':[4],
    'YearsSinceLastPromotion':[1],
    'JobChangeFrequency':[0.5],
    'TenureRatio':[0.5],
    'PromotionGap':[0.5],
    'MeanSatisfaction':[4],
    'SalaryCompetitiveness':[0.78],
    'RoleStabilityRatio':[0.2],
    'Education': [2],
    'EnvironmentSatisfaction':[4],
    'JobInvolvement':[3],
    'JobLevel':[4],
    'JobSatisfaction':[4],
    'RelationshipSatisfaction':[4],
    'StockOptionLevel':[1],
    'WorkLifeBalance':[3],
    'BusinessTravel_encoded':[1],
    'gender_encoded':[1],
    'Overtime_encoded':[0],
})

# Prediksi
prediksi = model.predict(df_new)

print("Hasil prediksi:", prediksi[0])
