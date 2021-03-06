/**
* Connected Vision - https://github.com/ConnectedVision
* MIT License
*/

// auto-generated header by CodeFromTemplate - Connected Vision - https://github.com/ConnectedVision
// CodeFromTemplate Version: 0.3 alpha
// Store_SQLite_ThumbnailGenerator_input_BoundingBox.h
// This file implements the IStore interface for SQLite access.
// It is generated once and will NOT be OVERWRITTEN by CodeFromTemplate.

#ifndef Store_SQLite_ThumbnailGenerator_input_BoundingBox_def
#define Store_SQLite_ThumbnailGenerator_input_BoundingBox_def

#include "stubs/Store_SQLite_Stub_ThumbnailGenerator_input_BoundingBox.h"

namespace ConnectedVision {
namespace Module {
namespace ThumbnailGenerator {
namespace DataHandling {

// if you want to extend the auto-generated class, enable the line below
//#define Store_SQLite_ThumbnailGenerator_input_BoundingBox_extended

#ifdef Store_SQLite_ThumbnailGenerator_input_BoundingBox_extended
/**
 * Store_SQLite_ThumbnailGenerator_input_BoundingBox
 *
 * module: Thumbnail Generator
 * description: rectangular region which is used for the cropping or for overlaying bounding boxes
 */
class Store_SQLite_ThumbnailGenerator_input_BoundingBox : public Store_SQLite_Stub_ThumbnailGenerator_input_BoundingBox {
public:
	/**
	* constructor
	*/
	Store_SQLite_ThumbnailGenerator_input_BoundingBox(
		const id_t& configID,			///< [in] config ID
		DBConnection& db				///< [in] DB connection object
	) : Store_SQLite_Stub_ThumbnailGenerator_input_BoundingBox ( configID, db )
	{}

	/*
	* virtual destructor
	*/
	virtual ~Store_SQLite_ThumbnailGenerator_input_BoundingBox()
	{}

 // TODO --> Your declarations and code comes HERE! <--

};
#endif // Store_SQLite_ThumbnailGenerator_input_BoundingBox_extended


// if you want to extend the auto-generated class, enable the line below
//#define Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox_extended

#ifdef Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox_extended
/**
 * factory for Store_SQLite_ThumbnailGenerator_input_BoundingBox
 */
class Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox : public Store_SQLite_Factory_Stub_ThumbnailGenerator_input_BoundingBox {
public:
	/**
	* constructor
	*/
	Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox(
		DBConnection& db				///< [in] DB connection object
	) : Store_SQLite_Factory_Stub_ThumbnailGenerator_input_BoundingBox ( db )
	{}

	/*
	* virtual destructor
	*/
	virtual ~Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox()
	{}

 // TODO --> Your declarations and code comes HERE! <--

};
#define Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox_enabled
#endif // Store_SQLite_Factory_ThumbnailGenerator_input_BoundingBox_extended

} // namespace DataHandling
} // namespace ThumbnailGenerator
} // namespace Module
} // namespace ConnectedVision

#include "stubs/Store_SQLite_ThumbnailGenerator_input_BoundingBox_Default.h"

#endif // Store_SQLite_ThumbnailGenerator_input_BoundingBox_def