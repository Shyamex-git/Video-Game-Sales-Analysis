import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_sales_column(df, column_name):
    """Cleans a sales column by removing 'M', '$', and converting to numeric."""
    if column_name in df.columns:
        df[column_name] = df[column_name].astype(str).str.replace('M', '', regex=False).str.replace('$', '', regex=False)
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce').fillna(0)
    return df

def visualize_query_1(file_path):
    """Visualizes Top Publisher by Genre."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Genre'])
    df = clean_sales_column(df, 'Sales_in_Genre')
    df = df.sort_values('Sales_in_Genre', ascending=True)

    plt.figure(figsize=(12, 8))
    plt.barh(df['Genre'], df['Sales_in_Genre'], color='skyblue')
    plt.xlabel('Total Sales (in Millions)')
    plt.ylabel('Genre')
    plt.title('Top Publisher Sales by Genre')
    plt.tight_layout()
    plt.savefig('Chart_Query_1_Top_Publisher_by_Genre.png')
    plt.close()
    print("Generated Chart for Query 1.")

def visualize_query_2(file_path):
    """Visualizes Platform Lifespan and Sales Analysis."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Platform'])
    df = clean_sales_column(df, 'Total_Global_Sales')

    plt.figure(figsize=(12, 8))
    plt.scatter(df['Lifespan_in_Years'], df['Total_Global_Sales'], alpha=0.7, s=df['Total_Global_Sales']/2)
    for _, row in df.nlargest(5, 'Total_Global_Sales').iterrows():
        plt.text(row['Lifespan_in_Years'] + 0.5, row['Total_Global_Sales'], row['Platform'])
    plt.xlabel('Platform Lifespan (Years)')
    plt.ylabel('Total Global Sales (in Millions)')
    plt.title('Platform Lifespan vs. Commercial Success')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('Chart_Query_2_Platform_Lifespan.png')
    plt.close()
    print("Generated Chart for Query 2.")

def visualize_query_3(file_path):
    """Visualizes Regional Taste - Comparing NA and Japan."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Genre'])
    df = clean_sales_column(df, 'North_America_Sales')
    df = clean_sales_column(df, 'Japan_Sales')
    df_sorted = df.sort_values(by='North_America_Sales', ascending=False).head(10)

    x = np.arange(len(df_sorted['Genre']))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 8))
    rects1 = ax.bar(x - width/2, df_sorted['North_America_Sales'], width, label='North America')
    rects2 = ax.bar(x + width/2, df_sorted['Japan_Sales'], width, label='Japan')

    ax.set_ylabel('Sales (in Millions)')
    ax.set_title('Genre Sales Comparison: North America vs. Japan (Top 10 NA Genres)')
    ax.set_xticks(x)
    ax.set_xticklabels(df_sorted['Genre'], rotation=45, ha='right')
    ax.legend()
    fig.tight_layout()
    plt.savefig('Chart_Query_3_Regional_Taste.png')
    plt.close()
    print("Generated Chart for Query 3.")

def visualize_query_4(file_path):
    """Visualizes Impact of Critic Scores on Sales."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Critic_Rating_Tier'])
    df = clean_sales_column(df, 'Average_Sales_per_Game')
    tier_order = ['A+ : Critically Acclaimed (90+)', 'B : Great Reviews (80-89)', 'C : Good Reviews (70-79)', 'D : Mixed Reviews (50-69)', 'F : Poor Reviews (<50)']
    df['Critic_Rating_Tier'] = pd.Categorical(df['Critic_Rating_Tier'], categories=tier_order, ordered=True)
    df = df.sort_values('Critic_Rating_Tier')

    plt.figure(figsize=(12, 7))
    plt.bar(df['Critic_Rating_Tier'], df['Average_Sales_per_Game'], color='mediumseagreen')
    plt.ylabel('Average Global Sales (in Millions)')
    plt.xlabel('Critic Rating Tier')
    plt.title('Impact of Critic Scores on Average Game Sales')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.savefig('Chart_Query_4_Critic_Scores.png')
    plt.close()
    print("Generated Chart for Query 4.")

def visualize_query_5(file_path):
    """Visualizes Genre Sales Performance by Decade."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Genre', 'Decade'])
    df = clean_sales_column(df, 'Total_Sales_in_Decade')
    pivot_df = df.pivot_table(index='Decade', columns='Genre', values='Total_Sales_in_Decade', aggfunc='sum').fillna(0)
    
    pivot_df.plot(kind='line', marker='o', figsize=(14, 8))
    plt.ylabel('Total Sales (in Millions)')
    plt.xlabel('Decade')
    plt.title('Evolution of Genre Popularity by Decade')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(title='Genre')
    plt.tight_layout()
    plt.savefig('Chart_Query_5_Genre_by_Decade.png')
    plt.close()
    print("Generated Chart for Query 5.")
    
def visualize_simple_query_1(file_path):
    """Visualizes Top Gaming Platforms."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Platform']).head(10)
    df = df.sort_values('Total_Sales_in_Millions', ascending=True)

    plt.figure(figsize=(12, 8))
    plt.barh(df['Platform'], df['Total_Sales_in_Millions'], color='c')
    plt.xlabel('Total Global Sales (in Millions)')
    plt.ylabel('Platform')
    plt.title('Top 10 Gaming Platforms by Global Sales')
    plt.tight_layout()
    plt.savefig('Chart_Simple_Query_1_Top_Platforms.png')
    plt.close()
    print("Generated Chart for Simple Query 1.")

def visualize_simple_query_2(file_path):
    """Visualizes Top-Selling Game Genres."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Genre']).head(10)
    df = df.sort_values('Total_Sales_in_Millions', ascending=True)

    plt.figure(figsize=(12, 8))
    plt.barh(df['Genre'], df['Total_Sales_in_Millions'], color='magenta')
    plt.xlabel('Total Global Sales (in Millions)')
    plt.ylabel('Genre')
    plt.title('Top 10 Game Genres by Global Sales')
    plt.tight_layout()
    plt.savefig('Chart_Simple_Query_2_Top_Genres.png')
    plt.close()
    print("Generated Chart for Simple Query 2.")

def visualize_simple_query_3(file_path):
    """Visualizes Top Publishers by Global Sales."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['Publisher']).head(10)
    df = df.sort_values('Total_Sales_in_Millions', ascending=True)

    plt.figure(figsize=(12, 8))
    plt.barh(df['Publisher'], df['Total_Sales_in_Millions'], color='orange')
    plt.xlabel('Total Global Sales (in Millions)')
    plt.ylabel('Publisher')
    plt.title('Top 10 Publishers by Global Sales')
    plt.tight_layout()
    plt.savefig('Chart_Simple_Query_3_Top_Publishers.png')
    plt.close()
    print("Generated Chart for Simple Query 3.")

def visualize_simple_query_4(file_path):
    """Visualizes Global Sales Trend Over the Years."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df['Year_of_Release'] = pd.to_numeric(df['Year_of_Release'], errors='coerce')
    df = df.dropna(subset=['Year_of_Release'])
    df = df.sort_values('Year_of_Release')

    plt.figure(figsize=(14, 7))
    plt.plot(df['Year_of_Release'], df['Total_Sales_in_Millions'], marker='.', linestyle='-')
    plt.xlabel('Year of Release')
    plt.ylabel('Total Global Sales (in Millions)')
    plt.title('Global Video Game Sales Trend Over the Years')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(rotation=45)
    plt.locator_params(axis='x', nbins=20)
    plt.tight_layout()
    plt.savefig('Chart_Simple_Query_4_Sales_Trend.png')
    plt.close()
    print("Generated Chart for Simple Query 4.")

# Main execution block
if __name__ == "__main__":
    queries_to_visualize = {
        'Query 1.csv': visualize_query_1,
        'Query 2.csv': visualize_query_2,
        'Query 3.csv': visualize_query_3,
        'Query 4.csv': visualize_query_4,
        'Query 5.csv': visualize_query_5,
        'Simple Query 1.csv': visualize_simple_query_1,
        'Simple Query 2.csv': visualize_simple_query_2,
        'Simple Query 3.csv': visualize_simple_query_3,
        'Simple Query 4.csv': visualize_simple_query_4,
    }

    print("--- Starting Visualization Generation ---")
    for path, func in queries_to_visualize.items():
        try:
            # Note: We need to handle the file content mismatch for the simple queries
            # based on your actual files. This code assumes they are named correctly.
            if path == 'Simple Query 1.csv':
                # This file actually contains Genre data
                temp_df = pd.read_csv(path)
                if 'Platform' not in temp_df.columns:
                    visualize_simple_query_2(path) # Use the genre visualizer
                else:
                    func(path)
            elif path == 'Simple Query 2.csv':
                # This file actually contains Platform data
                temp_df = pd.read_csv(path)
                if 'Genre' not in temp_df.columns:
                    visualize_simple_query_1(path) # Use the platform visualizer
                else:
                    func(path)
            else:
                func(path)
        except FileNotFoundError:
            print(f"Error: Could not find '{path}'. Skipping.")
        except Exception as e:
            print(f"An error occurred with '{path}': {e}")
    
    print("\n--- All visualizations have been generated and saved as PNG files! ---")