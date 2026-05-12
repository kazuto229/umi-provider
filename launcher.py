from providers.umi_kiro import UMIKiroProvider
from providers.umi_canva import UMICanvaProvider
from providers.umi_wavespeed import UMIWavespeedProvider

providers = [
    UMIKiroProvider(),
    UMICanvaProvider(),
    UMIWavespeedProvider()
]

print("Initializing UMI Gateway...")

for provider in providers:
    print(f"[READY] {provider.name}")

print("UMI Gateway started")