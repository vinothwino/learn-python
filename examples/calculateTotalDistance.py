def calculateTotalDistance(km,m):
    distanceInMeter=km*1000;
    distanceInMeter=(distanceInMeter+m)/4
    print(f'Total distance covered is {distanceInMeter}')

def main():
    totalKm=2;
    totalMeter=500;
    calculateTotalDistance(totalKm,totalMeter)

main()