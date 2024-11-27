import importlib
import pkgutil


def import_routers(package_name):
    def _import_subpackages(package, routers):
        for _, subpackage_name, is_pkg in pkgutil.iter_modules(package.__path__):
            full_package_name = f"{package.__name__}.{subpackage_name}"
            subpackage = importlib.import_module(full_package_name)
            if hasattr(subpackage, "endpoint"):
                routers.append(subpackage.endpoint)
            if is_pkg:
                _import_subpackages(subpackage, routers)

    package = importlib.import_module(package_name)
    routers = []
    _import_subpackages(package, routers)
    return routers
