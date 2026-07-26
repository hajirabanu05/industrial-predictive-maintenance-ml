from backend.services.dataset_stream import DatasetStreamer

streamer = DatasetStreamer()


def get_machine_sensor(machine_id: int):

    return streamer.get_machine_row(machine_id)