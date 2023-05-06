try:
    import grpc
    from concurrent import futures
    import time
    from function import calculator
    from grpc_generated_files import calculator_pb2 # GRPC Generated file
    from grpc_generated_files import calculator_pb2_grpc # GRPC Generated file

    print("All module loaded.....................")
except Exception as e:
    print("Error loading modules")

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    print("Starting Server...Listening to port 80...")
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()