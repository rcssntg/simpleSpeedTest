import speedtest


def perform_speed_test():
    st = speedtest.Speedtest()
    best_server = st.get_best_server()
    
    latency = best_server['latency']

    print('Testing download speed...')
    download_speed = st.download() / 1000000
    print('Testing upload speed...')
    upload_speed = st.upload() / 1000000
    
    return latency, download_speed, upload_speed



if __name__ == '__main__':
    latency, download_speed, upload_speed = perform_speed_test()
    print('Latency: {:.2f} ms'.format(latency))
    print('Download speed: {:.2f} Mbps'.format(download_speed))
    print('Upload speed: {:.2f} Mbps'.format(upload_speed))