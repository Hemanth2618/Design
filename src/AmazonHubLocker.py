from collections import defaultdict

LOCKER_SIZES = ['small', 'medium', 'large']

class Package:
    def __init__(self, package_id, package_size):
        self.package_id = package_id
        self.package_size = package_size
        self.locker = None

class Locker:
    def __init__(self, locker_id, locker_size):
        self.locker_id = locker_id
        self.locker_size = locker_size

class AmazonHubLocker:
    def __init__(self, lockers):
        self.emptyLockers = defaultdict(list)
        for locker in lockers:
            self.emptyLockers[locker.locker_size].append(locker)
        self.storedPackages = dict()

    def storePackage(self, package):
        flag = False
        for size in LOCKER_SIZES:
            if package.package_size < size:
                if len(self.emptyLockers):
                    assigned_locker = self.emptyLockers[size].pop()
                    flag = True
        if flag:
            package.locker = assigned_locker
        self.storedPackages[package.package_id] = package
        print(self.storedPackages)
        return package.package_id

    def pickupPackage(self, package):
        if package.package_id not in self.storedPackages:
            return None
        curr_package = self.storedPackages[package.package_id]
        curr_locker = curr_package.locker
        self.emptyLockers[curr_locker.locker_size].append(curr_locker)
        return curr_package.package_id

if __name__ == '__main__':
    in_store_lockers = [Locker(100, 'small'), Locker(110, 'medium'), Locker(150, 'large'), Locker(120, 'small')]
    a = AmazonHubLocker(in_store_lockers)
    p1 = Package(1, 'small')
    p2 = Package(2, 'medium')
    p3 = Package(3, 'large')
    print(a.storePackage(p1))
    print(a.storePackage(p3))
    print(a.pickupPackage(p1))
