from modelscope import snapshot_download
model_dir = snapshot_download("Qwen/Qwen-1_8B-Chat", revision = "v1.0.0", cache_dir='model')
