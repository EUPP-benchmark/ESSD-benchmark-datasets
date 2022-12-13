
conda activate ESSD-benchmark-datasets
echo "Extracting ESSD test data from the EUMETNET EUPPBench benchmark dataset..."
python extract_ESSD_benchmark_test_data.py
echo "Done !"
echo "Extracting ESSD training data from the EUMETNET EUPPBench benchmark dataset..."
python extract_ESSD_benchmark_training_data.py
echo "Done !"
conda deactivate
rm *.npy station_id_order.txt
