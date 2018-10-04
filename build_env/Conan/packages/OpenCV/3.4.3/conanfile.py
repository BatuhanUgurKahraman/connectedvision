import glob
import os
import re
from conans import CMake, ConanFile, tools



class OpenCV(ConanFile):
	name = "OpenCV"
	version = "3.4.3"
	license = "3-clause BSD License, http://opencv.org/license.html"
	url = "http://opencv.org"
	settings = {"os": ["Windows", "Linux"], "compiler": ["Visual Studio", "gcc"], "arch": ["x86", "x86_64", "armv7hf"], "build_type": ["Debug", "Release"]}
	options = {
		"BUILD_DOCS": [True, False],
		"BUILD_EXAMPLES": [True, False],
		"BUILD_JASPER": [True, False],
		"BUILD_JPEG": [True, False],
		"BUILD_opencv_apps": [True, False],
		"BUILD_PERF_TESTS": [True, False],
		"BUILD_PNG": [True, False],
		"BUILD_TESTS": [True, False],
		"BUILD_TIFF": [True, False],
		"BUILD_ZLIB": [True, False],
		"WITH_1394": [True, False],
		"WITH_CLP": [True, False],
		"WITH_CSTRIPES": [True, False],
		"WITH_CUBLAS": [True, False],
		"WITH_CUDA": [True, False],
		"WITH_CUFFT": [True, False],
		"WITH_DIRECTX": [True, False],
		"WITH_EIGEN": [True, False],
		"WITH_FFMPEG": [True, False],
		"WITH_GDAL": [True, False],
		"WITH_GIGEAPI": [True, False],
		"WITH_GPHOTO2": [True, False],
		"WITH_GSTREAMER": [True, False],
		"WITH_GSTREAMER_0_10": [True, False],
		"WITH_GTK": [True, False],
		"WITH_GTK_2_X": [True, False],
		"WITH_IMGCODEC_HDR": [True, False],
		"WITH_IMGCODEC_SUNRASTER": [True, False],
		"WITH_IMGCODEC_PXM": [True, False],
		"WITH_INF_ENGINE": [True, False],
		"WITH_INTELPERC": [True, False],
		"WITH_IPP": [True, False],
		"WITH_JASPER": [True, False],
		"WITH_JPEG": [True, False],
		"WITH_MATLAB": [True, False],
		"WITH_NVCUVID": [True, False],
		"WITH_OPENCL": [True, False],
		"WITH_OPENCLAMDBLAS": [True, False],
		"WITH_OPENCLAMDFFT": [True, False],
		"WITH_OPENCL_SVM": [True, False],
		"WITH_OPENEXR": [True, False],
		"WITH_OPENGL": [True, False],
		"WITH_OPENMP": [True, False],
		"WITH_OPENNI": [True, False],
		"WITH_OPENNI2": [True, False],
		"WITH_OPENVX": [True, False],
		"WITH_PNG": [True, False],
		"WITH_PVAPI": [True, False],
		"WITH_PROTOBUF": [True, False],
		"WITH_QT": [True, False],
		"WITH_TBB": [True, False],
		"WITH_TIFF": [True, False],
		"WITH_UNICAP": [True, False],
		"WITH_VA": [True, False],
		"WITH_VA_INTEL": [True, False],
		"WITH_VTK": [True, False],
		"WITH_WEBP": [True, False],
		"WITH_XIMEA": [True, False],
		"WITH_XINE": [True, False],
		"WITH_ZLIB": [True, False]
	}
	default_options = '''
BUILD_DOCS=False
BUILD_EXAMPLES=False
BUILD_JASPER=True
BUILD_JPEG=True
BUILD_opencv_apps=False
BUILD_PERF_TESTS=False
BUILD_PNG=True
BUILD_TESTS=False
BUILD_TIFF=True
BUILD_ZLIB=False
WITH_1394=False
WITH_CLP=False
WITH_CSTRIPES=False
WITH_CUBLAS=False
WITH_CUDA=False
WITH_CUFFT=False
WITH_DIRECTX=False
WITH_EIGEN=False
WITH_FFMPEG=True
WITH_GDAL=False
WITH_GIGEAPI=False
WITH_GPHOTO2=False
WITH_GSTREAMER=False
WITH_GSTREAMER_0_10=False
WITH_GTK=False
WITH_GTK_2_X=False
WITH_IMGCODEC_HDR=True
WITH_IMGCODEC_SUNRASTER=True
WITH_IMGCODEC_PXM=True
WITH_INF_ENGINE=False
WITH_INTELPERC=False
WITH_IPP=False
WITH_JASPER=True
WITH_JPEG=True
WITH_MATLAB=False
WITH_NVCUVID=False
WITH_OPENCL=True
WITH_OPENCLAMDBLAS=False
WITH_OPENCLAMDFFT=False
WITH_OPENCL_SVM=False
WITH_OPENEXR=False
WITH_OPENGL=False
WITH_OPENMP=False
WITH_OPENNI2=False
WITH_OPENVX=False
WITH_OPENNI=False
WITH_PNG=True
WITH_PVAPI=False
WITH_PROTOBUF=True
WITH_QT=False
WITH_TBB=False
WITH_TIFF=True
WITH_UNICAP=False
WITH_VA=False
WITH_VA_INTEL=False
WITH_VTK=False
WITH_WEBP=True
WITH_XIMEA=False
WITH_XINE=False
WITH_ZLIB=True
'''
	
	
	def getInstallDir(self):
		return os.path.join(self.name, "build", "install")



	def getSubdirectories(self, d):
		return [ f for f in os.listdir(d) if os.path.isdir(f) ]



	def requirements(self):
		self.output.info("")
		self.output.info("---------- requirements ----------")
		self.output.info("")
		
		self.requires("FFmpeg/3.2.4@covi/stable", private=False)
		
		if not self.options.BUILD_ZLIB:
			self.requires("zlib/1.2.11@covi/stable", private=False)


	def source(self):
		self.output.info("")
		self.output.info("---------- source ----------")
		self.output.info("")
		
		filename = self.version + ".zip"
		url = "https://github.com/opencv/opencv/archive/" + filename
		self.output.info("downloading " + url + " ...")
		tools.download(url, filename, retry=3, retry_wait=10)
		tools.unzip(filename)
		os.remove(filename)
		dirnames = self.getSubdirectories(self.source_folder)
		os.rename(dirnames[0], self.name)	



	def build(self): 
		self.output.info("")
		self.output.info("---------- build ----------")
		self.output.info("")
		self.output.info("os        : " + str(self.settings.os))
		self.output.info("arch      : " + str(self.settings.arch))
		self.output.info("build_type: " + str(self.settings.build_type))
		
		if self.settings.compiler == "Visual Studio":
			self.output.info("runtime   : " + str(self.settings.compiler.runtime))
		
		# create options dict for CMake command
		opts = dict()
		
		# extract the options dict from the options variable in order to append additional values
		for item in self.options.items():
			opts[item[0]] = item[1]
		
		# not included in conan options since it has not been implemented/tested
		opts["BUILD_SHARED_LIBS"] = False
		opts["INSTALL_CREATE_DISTRIB"] = True
		
		# use already existing conan zlib package
		if opts["BUILD_ZLIB"] == "False":
			zlibRootDir = self.deps_cpp_info["zlib"].rootpath
			opts["ZLIB_INCLUDE_DIR"] = os.path.join(zlibRootDir, self.deps_cpp_info["zlib"].includedirs[0])
			
			libDir = os.path.join(zlibRootDir, self.deps_cpp_info["zlib"].libdirs[0])
			
			libFiles = [filename for filename in os.listdir(libDir) if re.match("^(lib)?" + self.deps_cpp_info["zlib"].libs[0] + r"\.(a|lib)", filename)]
			
			if not libFiles:
				raise Exception("zlib (Conan package, not the OpenCV 3rdparty version) was not found in: " + libDir)
			
			opts["ZLIB_LIBRARY"] = os.path.join(libDir, libFiles[0])
			
			# replace backslash path separators for Windows with forward slashes to avoid linker problems with unknown escape sequences
			if self.settings.os == "Windows":
				opts["ZLIB_LIBRARY"] = opts["ZLIB_LIBRARY"].replace("\\", "/")
		
		if opts["WITH_FFMPEG"] == "True":
			opts["FFMPEG_FOUND"] = True
			opts["FFMPEG_INCLUDE_DIRS"] = self.deps_cpp_info["FFmpeg"].include_paths[0]
			opts["FFMPEG_LIBRARY_DIRS"] = self.deps_cpp_info["FFmpeg"].lib_paths[0]
			opts["FFMPEG_LIBRARIES"] = ";".join(self.deps_cpp_info["FFmpeg"].libs)
			
			for lib in self.deps_cpp_info["FFmpeg"].libs:
				opts["FFMPEG_" + lib + "_FOUND"] = True		
		
		if self.settings.compiler == "Visual Studio":
			opts["BUILD_WITH_STATIC_CRT"] = self.settings.compiler.runtime in ["MT", "MTd"]
		
		opts["CMAKE_INSTALL_PREFIX"] = os.path.basename(self.getInstallDir())

		buildDir = os.path.join(self.name, "build")
		os.makedirs(buildDir)

		cmake = CMake(self)
		cmake.configure(defs=opts, source_folder=self.name, build_folder=buildDir)
		cmake.build(target="install")



	def package(self):
		self.output.info("")
		self.output.info("---------- package ----------")
		self.output.info("")
		
		installDir = os.path.join(self.name, "build", "install")

		self.copy(pattern="*.h*", dst="include", src=os.path.join(installDir, "include"), keep_path=True)

		if self.settings.os == "Windows":
			self.copy(pattern="*.lib", dst="lib", src=installDir, keep_path=False)
		else:
			self.copy(pattern="*.a", dst="lib", src=installDir, keep_path=False)



	def package_info(self):
		self.output.info("")
		self.output.info("---------- package_info ----------")
		self.output.info("")
		
		libDir = os.path.join(self.package_folder, self.cpp_info.libdirs[0])
		
		with tools.chdir(libDir):
			if self.settings.os == "Windows":
				self.cpp_info.libs = glob.glob("*.lib")
			else:
				libsAllUnsorted = glob.glob("*.a")

				libsCv = []
				libs3rd = []
				r = re.compile(r"lib(opencv_.*)\.a")

				for f in libsAllUnsorted:
					if re.match(r, f):
						libsCv.append(re.match(r, f).group(1))
					else:
						libs3rd.append(re.match(r"lib(.*)\.a", f).group(1))
				
				libsCvSubsetSorted = ["opencv_imgproc", "opencv_core"]

				for lib in libsCvSubsetSorted:
					if lib in libsCv:
						libsCv.remove(lib)
						libsCv.append(lib)
				
				self.cpp_info.libs = libsCv + libs3rd