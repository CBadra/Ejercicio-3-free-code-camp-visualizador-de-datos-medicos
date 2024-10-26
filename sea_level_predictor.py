import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer datos del archivo
    df = pd.read_csv('epa-sea-level.csv')

    # Crear gráfico de dispersión
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Crear la primera línea de mejor ajuste (desde el inicio hasta el año 2050)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Predecir hasta 2050 para la primera línea
    years_extended = pd.Series(range(1880, 2051))  # Años desde 1880 hasta 2050
    sea_level_predicted = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_predicted, color='red', label='Best Fit Line (1880-2050)')

    # Crear la segunda línea de mejor ajuste (desde el año 2000 hasta el más reciente en los datos)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Predecir hasta 2050 solo para los años desde 2000
    years_2000_extended = pd.Series(range(2000, 2051))  # Años desde 2000 hasta 2050
    sea_level_predicted_2000 = slope_2000 * years_2000_extended + intercept_2000
    plt.plot(years_2000_extended, sea_level_predicted_2000, color='green', label='Best Fit Line (2000-2050)')

    # Añadir etiquetas y título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Guardar gráfico y devolver datos para la prueba
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Llamar a la función para probar
if __name__ == "__main__":
    draw_plot()
    plt.show()  # Muestra la figura al ejecutar directamente
