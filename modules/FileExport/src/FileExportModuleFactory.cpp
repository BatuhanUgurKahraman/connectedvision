/**
* Connected Vision - https://github.com/ConnectedVision
* MIT License
*/

#include "FileExportModuleFactory.h"
#include "FileExportModule.h"

namespace ConnectedVision {
namespace Module {
namespace FileExport {

ConnectedVision::shared_ptr<IModule> FileExportModuleFactory::createModule()
{
	ConnectedVision::shared_ptr<IModule> moduleInstance = boost::dynamic_pointer_cast<IModule>(ConnectedVision::make_shared<FileExportModule>());
	if ( !moduleInstance ) 
		throw std::runtime_error("FileExportModuleFactory: error creating instance for module: FileExport");

	return moduleInstance;
}

} // namespace FileExport
} // namespace Module
} // namespace ConnectedVision