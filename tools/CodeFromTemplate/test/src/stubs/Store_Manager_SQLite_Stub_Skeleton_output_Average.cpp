// auto-generated header by CodeFromTemplate - Connected Vision - https://github.com/ConnectedVision
// CodeFromTemplate Version: 0.3 alpha
// 
// NEVER TOUCH this file!

#include <exception>
#include <boost/assign/list_of.hpp>

#include "Store_Manager_SQLite_Stub_Skeleton_output_Average.h"

// --> Do NOT EDIT <--
namespace ConnectedVision {
namespace test {
namespace DataHandling {

// --> Do NOT EDIT <--
int Store_Manager_SQLite_Stub_Skeleton_output_Average::creationCount = 0;

// --> Do NOT EDIT <--
Store_Manager_SQLite_Stub_Skeleton_output_Average::Store_Manager_SQLite_Stub_Skeleton_output_Average( DBConnection& db ) : 
	Store_Manager_Basic<Class_Skeleton_output_Average>( boost::dynamic_pointer_cast< ConnectedVision::DataHandling::IStore_ReadWrite_Factory<Class_Skeleton_output_Average> >( make_shared<Store_SQLite_Factory_Skeleton_output_Average>( db	)) )
{
	if ( creationCount > 0 )
	{
		// we have one instance already
		throw ConnectedVision::runtime_error("just one instance of Store_Manager_SQLite_Stub_Skeleton_output_Average allowed");
	}
	creationCount = 1;
}

// --> Do NOT EDIT <--
Store_Manager_SQLite_Stub_Skeleton_output_Average::~Store_Manager_SQLite_Stub_Skeleton_output_Average()
{
	creationCount = 0; 
}

} // namespace DataHandling
} // namespace test
} // namespace ConnectedVision