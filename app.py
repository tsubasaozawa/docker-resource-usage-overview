from src.data_fetcher import get_system_data
from src.data_parser import parse_docker_df_data
from src.chart_generator import create_bar_chart

if __name__ == "__main__":
    cmd = ['docker', 'system', 'df']
    
    if cmd == ['docker', 'system', 'df']:
        docker_data = get_system_data(cmd)
        if docker_data:
            print('The result data of executing docker system df command:\n', docker_data)

            labels, values = parse_docker_df_data(docker_data)
            create_bar_chart(labels, values)
        else:
            print("Failed to retrieve docker system df data.")
    else:
        print(f"Unknown command: {cmd}")