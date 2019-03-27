# CMake generated Testfile for 
# Source directory: /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg
# Build directory: /home/chaos/Scouting-2019-Python/.buildozer/android/platform/build/build/other_builds/jpeg/armeabi-v7a__ndk_target_21/jpeg
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(tjunittest-static "tjunittest-static")
add_test(tjunittest-static-alloc "tjunittest-static" "-alloc")
add_test(tjunittest-static-yuv "tjunittest-static" "-yuv")
add_test(tjunittest-static-yuv-alloc "tjunittest-static" "-yuv" "-alloc")
add_test(tjunittest-static-yuv-nopad "tjunittest-static" "-yuv" "-noyuvpad")
add_test(tjunittest-static-bmp "tjunittest-static" "-bmp")
add_test(tjbench-static-tile-cp "/usr/bin/cmake" "-E" "copy_if_different" "testimages/testorig.ppm" "testout_tile.ppm")
add_test(tjbench-static-tile "tjbench-static" "testout_tile.ppm" "95" "-rgb" "-quiet" "-tile" "-benchtime" "0.01" "-warmup" "0")
set_tests_properties(tjbench-static-tile PROPERTIES  DEPENDS "tjbench-static-tile-cp")
add_test(tjbench-static-tile-gray-8x8-cmp "md5/md5cmp" "89d3ca21213d9d864b50b4e4e7de4ca6" "testout_tile_GRAY_Q95_8x8.ppm")
set_tests_properties(tjbench-static-tile-gray-8x8-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-420-8x8-cmp "md5/md5cmp" "847fceab15c5b7b911cb986cf0f71de3" "testout_tile_420_Q95_8x8.ppm")
set_tests_properties(tjbench-static-tile-420-8x8-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-422-8x8-cmp "md5/md5cmp" "d83dacd9fc73b0a6f10c09acad64eb1e" "testout_tile_422_Q95_8x8.ppm")
set_tests_properties(tjbench-static-tile-422-8x8-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-444-8x8-cmp "md5/md5cmp" "7964e41e67cfb8d0a587c0aa4798f9c3" "testout_tile_444_Q95_8x8.ppm")
set_tests_properties(tjbench-static-tile-444-8x8-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-gray-16x16-cmp "md5/md5cmp" "89d3ca21213d9d864b50b4e4e7de4ca6" "testout_tile_GRAY_Q95_16x16.ppm")
set_tests_properties(tjbench-static-tile-gray-16x16-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-420-16x16-cmp "md5/md5cmp" "ca45552a93687e078f7137cc4126a7b0" "testout_tile_420_Q95_16x16.ppm")
set_tests_properties(tjbench-static-tile-420-16x16-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-422-16x16-cmp "md5/md5cmp" "35077fb610d72dd743b1eb0cbcfe10fb" "testout_tile_422_Q95_16x16.ppm")
set_tests_properties(tjbench-static-tile-422-16x16-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-444-16x16-cmp "md5/md5cmp" "7964e41e67cfb8d0a587c0aa4798f9c3" "testout_tile_444_Q95_16x16.ppm")
set_tests_properties(tjbench-static-tile-444-16x16-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-gray-32x32-cmp "md5/md5cmp" "89d3ca21213d9d864b50b4e4e7de4ca6" "testout_tile_GRAY_Q95_32x32.ppm")
set_tests_properties(tjbench-static-tile-gray-32x32-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-420-32x32-cmp "md5/md5cmp" "d8676f1d6b68df358353bba9844f4a00" "testout_tile_420_Q95_32x32.ppm")
set_tests_properties(tjbench-static-tile-420-32x32-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-422-32x32-cmp "md5/md5cmp" "e6902ed8a449ecc0f0d6f2bf945f65f7" "testout_tile_422_Q95_32x32.ppm")
set_tests_properties(tjbench-static-tile-422-32x32-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-444-32x32-cmp "md5/md5cmp" "7964e41e67cfb8d0a587c0aa4798f9c3" "testout_tile_444_Q95_32x32.ppm")
set_tests_properties(tjbench-static-tile-444-32x32-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-gray-64x64-cmp "md5/md5cmp" "89d3ca21213d9d864b50b4e4e7de4ca6" "testout_tile_GRAY_Q95_64x64.ppm")
set_tests_properties(tjbench-static-tile-gray-64x64-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-420-64x64-cmp "md5/md5cmp" "4e4c1a3d7ea4bace4f868bcbe83b7050" "testout_tile_420_Q95_64x64.ppm")
set_tests_properties(tjbench-static-tile-420-64x64-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-422-64x64-cmp "md5/md5cmp" "2b4502a8f316cedbde1da7bce3d2231e" "testout_tile_422_Q95_64x64.ppm")
set_tests_properties(tjbench-static-tile-422-64x64-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-444-64x64-cmp "md5/md5cmp" "7964e41e67cfb8d0a587c0aa4798f9c3" "testout_tile_444_Q95_64x64.ppm")
set_tests_properties(tjbench-static-tile-444-64x64-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-gray-128x128-cmp "md5/md5cmp" "89d3ca21213d9d864b50b4e4e7de4ca6" "testout_tile_GRAY_Q95_128x128.ppm")
set_tests_properties(tjbench-static-tile-gray-128x128-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-420-128x128-cmp "md5/md5cmp" "f24c3429c52265832beab9df72a0ceae" "testout_tile_420_Q95_128x128.ppm")
set_tests_properties(tjbench-static-tile-420-128x128-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-422-128x128-cmp "md5/md5cmp" "f0b5617d578f5e13c8eee215d64d4877" "testout_tile_422_Q95_128x128.ppm")
set_tests_properties(tjbench-static-tile-422-128x128-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tile-444-128x128-cmp "md5/md5cmp" "7964e41e67cfb8d0a587c0aa4798f9c3" "testout_tile_444_Q95_128x128.ppm")
set_tests_properties(tjbench-static-tile-444-128x128-cmp PROPERTIES  DEPENDS "tjbench-static-tile")
add_test(tjbench-static-tilem-cp "/usr/bin/cmake" "-E" "copy_if_different" "testimages/testorig.ppm" "testout_tilem.ppm")
add_test(tjbench-static-tilem "tjbench-static" "testout_tilem.ppm" "95" "-rgb" "-fastupsample" "-quiet" "-tile" "-benchtime" "0.01" "-warmup" "0")
set_tests_properties(tjbench-static-tilem PROPERTIES  DEPENDS "tjbench-static-tilem-cp")
add_test(tjbench-static-tile-420m-8x8-cmp "md5/md5cmp" "bc25320e1f4c31ce2e610e43e9fd173c" "testout_tilem_420_Q95_8x8.ppm")
set_tests_properties(tjbench-static-tile-420m-8x8-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-422m-8x8-cmp "md5/md5cmp" "828941d7f41cd6283abd6beffb7fd51d" "testout_tilem_422_Q95_8x8.ppm")
set_tests_properties(tjbench-static-tile-422m-8x8-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-420m-16x16-cmp "md5/md5cmp" "75ffdf14602258c5c189522af57fa605" "testout_tilem_420_Q95_16x16.ppm")
set_tests_properties(tjbench-static-tile-420m-16x16-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-422m-16x16-cmp "md5/md5cmp" "e877ae1324c4a280b95376f7f018172f" "testout_tilem_422_Q95_16x16.ppm")
set_tests_properties(tjbench-static-tile-422m-16x16-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-420m-32x32-cmp "md5/md5cmp" "75ffdf14602258c5c189522af57fa605" "testout_tilem_420_Q95_32x32.ppm")
set_tests_properties(tjbench-static-tile-420m-32x32-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-422m-32x32-cmp "md5/md5cmp" "e877ae1324c4a280b95376f7f018172f" "testout_tilem_422_Q95_32x32.ppm")
set_tests_properties(tjbench-static-tile-422m-32x32-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-420m-64x64-cmp "md5/md5cmp" "75ffdf14602258c5c189522af57fa605" "testout_tilem_420_Q95_64x64.ppm")
set_tests_properties(tjbench-static-tile-420m-64x64-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-422m-64x64-cmp "md5/md5cmp" "e877ae1324c4a280b95376f7f018172f" "testout_tilem_422_Q95_64x64.ppm")
set_tests_properties(tjbench-static-tile-422m-64x64-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-420m-128x128-cmp "md5/md5cmp" "75ffdf14602258c5c189522af57fa605" "testout_tilem_420_Q95_128x128.ppm")
set_tests_properties(tjbench-static-tile-420m-128x128-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(tjbench-static-tile-422m-128x128-cmp "md5/md5cmp" "e877ae1324c4a280b95376f7f018172f" "testout_tilem_422_Q95_128x128.ppm")
set_tests_properties(tjbench-static-tile-422m-128x128-cmp PROPERTIES  DEPENDS "tjbench-static-tilem")
add_test(cjpeg-static-rgb-islow "cjpeg-static" "-rgb" "-dct" "int" "-icc" "testimages/test1.icc" "-outfile" "testout_rgb_islow.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-rgb-islow-cmp "md5/md5cmp" "1d44a406f61da743b5fd31c0a9abdca3" "testout_rgb_islow.jpg")
set_tests_properties(cjpeg-static-rgb-islow-cmp PROPERTIES  DEPENDS "cjpeg-static-rgb-islow")
add_test(djpeg-static-rgb-islow "djpeg-static" "-dct" "int" "-ppm" "-icc" "testout_rgb_islow.icc" "-outfile" "testout_rgb_islow.ppm" "testout_rgb_islow.jpg")
set_tests_properties(djpeg-static-rgb-islow PROPERTIES  DEPENDS "cjpeg-static-rgb-islow")
add_test(djpeg-static-rgb-islow-cmp "md5/md5cmp" "00a257f5393fef8821f2b88ac7421291" "testout_rgb_islow.ppm")
set_tests_properties(djpeg-static-rgb-islow-cmp PROPERTIES  DEPENDS "djpeg-static-rgb-islow")
add_test(djpeg-static-rgb-islow-icc-cmp "md5/md5cmp" "b06a39d730129122e85c1363ed1bbc9e" "testout_rgb_islow.icc")
add_test(jpegtran-static-icc "jpegtran-static" "-copy" "all" "-icc" "testimages/test2.icc" "-outfile" "testout_rgb_islow2.jpg" "testout_rgb_islow.jpg")
add_test(jpegtran-static-icc-cmp "md5/md5cmp" "31d121e57b6c2934c890a7fc7763bcd4" "testout_rgb_islow2.jpg")
set_tests_properties(jpegtran-static-icc-cmp PROPERTIES  DEPENDS "jpegtran-static-icc")
add_test(djpeg-static-rgb-islow-565 "djpeg-static" "-dct" "int" "-rgb565" "-dither" "none" "-bmp" "-outfile" "testout_rgb_islow_565.bmp" "testout_rgb_islow.jpg")
set_tests_properties(djpeg-static-rgb-islow-565 PROPERTIES  DEPENDS "cjpeg-static-rgb-islow")
add_test(djpeg-static-rgb-islow-565-cmp "md5/md5cmp" "f07d2e75073e4bb10f6c6f4d36e2e3be" "testout_rgb_islow_565.bmp")
set_tests_properties(djpeg-static-rgb-islow-565-cmp PROPERTIES  DEPENDS "djpeg-static-rgb-islow-565")
add_test(djpeg-static-rgb-islow-565D "djpeg-static" "-dct" "int" "-rgb565" "-bmp" "-outfile" "testout_rgb_islow_565D.bmp" "testout_rgb_islow.jpg")
set_tests_properties(djpeg-static-rgb-islow-565D PROPERTIES  DEPENDS "cjpeg-static-rgb-islow")
add_test(djpeg-static-rgb-islow-565D-cmp "md5/md5cmp" "4cfa0928ef3e6bb626d7728c924cfda4" "testout_rgb_islow_565D.bmp")
set_tests_properties(djpeg-static-rgb-islow-565D-cmp PROPERTIES  DEPENDS "djpeg-static-rgb-islow-565D")
add_test(cjpeg-static-422-ifast-opt "cjpeg-static" "-sample" "2x1" "-dct" "fast" "-opt" "-outfile" "testout_422_ifast_opt.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-422-ifast-opt-cmp "md5/md5cmp" "2540287b79d913f91665e660303ab2c8" "testout_422_ifast_opt.jpg")
set_tests_properties(cjpeg-static-422-ifast-opt-cmp PROPERTIES  DEPENDS "cjpeg-static-422-ifast-opt")
add_test(djpeg-static-422-ifast "djpeg-static" "-dct" "fast" "-outfile" "testout_422_ifast.ppm" "testout_422_ifast_opt.jpg")
set_tests_properties(djpeg-static-422-ifast PROPERTIES  DEPENDS "cjpeg-static-422-ifast-opt")
add_test(djpeg-static-422-ifast-cmp "md5/md5cmp" "35bd6b3f833bad23de82acea847129fa" "testout_422_ifast.ppm")
set_tests_properties(djpeg-static-422-ifast-cmp PROPERTIES  DEPENDS "djpeg-static-422-ifast")
add_test(djpeg-static-422m-ifast "djpeg-static" "-dct" "fast" "-nosmooth" "-outfile" "testout_422m_ifast.ppm" "testout_422_ifast_opt.jpg")
set_tests_properties(djpeg-static-422m-ifast PROPERTIES  DEPENDS "cjpeg-static-422-ifast-opt")
add_test(djpeg-static-422m-ifast-cmp "md5/md5cmp" "8dbc65323d62cca7c91ba02dd1cfa81d" "testout_422m_ifast.ppm")
set_tests_properties(djpeg-static-422m-ifast-cmp PROPERTIES  DEPENDS "djpeg-static-422m-ifast")
add_test(djpeg-static-422m-ifast-565 "djpeg-static" "-dct" "int" "-nosmooth" "-rgb565" "-dither" "none" "-bmp" "-outfile" "testout_422m_ifast_565.bmp" "testout_422_ifast_opt.jpg")
set_tests_properties(djpeg-static-422m-ifast-565 PROPERTIES  DEPENDS "cjpeg-static-422-ifast-opt")
add_test(djpeg-static-422m-ifast-565-cmp "md5/md5cmp" "3294bd4d9a1f2b3d08ea6020d0db7065" "testout_422m_ifast_565.bmp")
set_tests_properties(djpeg-static-422m-ifast-565-cmp PROPERTIES  DEPENDS "djpeg-static-422m-ifast-565")
add_test(djpeg-static-422m-ifast-565D "djpeg-static" "-dct" "int" "-nosmooth" "-rgb565" "-bmp" "-outfile" "testout_422m_ifast_565D.bmp" "testout_422_ifast_opt.jpg")
set_tests_properties(djpeg-static-422m-ifast-565D PROPERTIES  DEPENDS "cjpeg-static-422-ifast-opt")
add_test(djpeg-static-422m-ifast-565D-cmp "md5/md5cmp" "da98c9c7b6039511be4a79a878a9abc1" "testout_422m_ifast_565D.bmp")
set_tests_properties(djpeg-static-422m-ifast-565D-cmp PROPERTIES  DEPENDS "djpeg-static-422m-ifast-565D")
add_test(cjpeg-static-420-q100-ifast-prog "cjpeg-static" "-sample" "2x2" "-quality" "100" "-dct" "fast" "-prog" "-outfile" "testout_420_q100_ifast_prog.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-420-q100-ifast-prog-cmp "md5/md5cmp" "990cbe0329c882420a2094da7e5adade" "testout_420_q100_ifast_prog.jpg")
set_tests_properties(cjpeg-static-420-q100-ifast-prog-cmp PROPERTIES  DEPENDS "cjpeg-static-420-q100-ifast-prog")
add_test(djpeg-static-420-q100-ifast-prog "djpeg-static" "-dct" "fast" "-outfile" "testout_420_q100_ifast.ppm" "testout_420_q100_ifast_prog.jpg")
set_tests_properties(djpeg-static-420-q100-ifast-prog PROPERTIES  DEPENDS "cjpeg-static-420-q100-ifast-prog")
add_test(djpeg-static-420-q100-ifast-prog-cmp "md5/md5cmp" "5a732542015c278ff43635e473a8a294" "testout_420_q100_ifast.ppm")
set_tests_properties(djpeg-static-420-q100-ifast-prog-cmp PROPERTIES  DEPENDS "djpeg-static-420-q100-ifast-prog")
add_test(djpeg-static-420m-q100-ifast-prog "djpeg-static" "-dct" "fast" "-nosmooth" "-outfile" "testout_420m_q100_ifast.ppm" "testout_420_q100_ifast_prog.jpg")
set_tests_properties(djpeg-static-420m-q100-ifast-prog PROPERTIES  DEPENDS "cjpeg-static-420-q100-ifast-prog")
add_test(djpeg-static-420m-q100-ifast-prog-cmp "md5/md5cmp" "ff692ee9323a3b424894862557c092f1" "testout_420m_q100_ifast.ppm")
set_tests_properties(djpeg-static-420m-q100-ifast-prog-cmp PROPERTIES  DEPENDS "djpeg-static-420m-q100-ifast-prog")
add_test(cjpeg-static-gray-islow "cjpeg-static" "-gray" "-dct" "int" "-outfile" "testout_gray_islow.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-gray-islow-cmp "md5/md5cmp" "72b51f894b8f4a10b3ee3066770aa38d" "testout_gray_islow.jpg")
set_tests_properties(cjpeg-static-gray-islow-cmp PROPERTIES  DEPENDS "cjpeg-static-gray-islow")
add_test(djpeg-static-gray-islow "djpeg-static" "-dct" "int" "-outfile" "testout_gray_islow.ppm" "testout_gray_islow.jpg")
set_tests_properties(djpeg-static-gray-islow PROPERTIES  DEPENDS "cjpeg-static-gray-islow")
add_test(djpeg-static-gray-islow-cmp "md5/md5cmp" "8d3596c56eace32f205deccc229aa5ed" "testout_gray_islow.ppm")
set_tests_properties(djpeg-static-gray-islow-cmp PROPERTIES  DEPENDS "djpeg-static-gray-islow")
add_test(djpeg-static-gray-islow-rgb "djpeg-static" "-dct" "int" "-rgb" "-outfile" "testout_gray_islow_rgb.ppm" "testout_gray_islow.jpg")
set_tests_properties(djpeg-static-gray-islow-rgb PROPERTIES  DEPENDS "cjpeg-static-gray-islow")
add_test(djpeg-static-gray-islow-rgb-cmp "md5/md5cmp" "116424ac07b79e5e801f00508eab48ec" "testout_gray_islow_rgb.ppm")
set_tests_properties(djpeg-static-gray-islow-rgb-cmp PROPERTIES  DEPENDS "djpeg-static-gray-islow-rgb")
add_test(djpeg-static-gray-islow-565 "djpeg-static" "-dct" "int" "-rgb565" "-dither" "none" "-bmp" "-outfile" "testout_gray_islow_565.bmp" "testout_gray_islow.jpg")
set_tests_properties(djpeg-static-gray-islow-565 PROPERTIES  DEPENDS "cjpeg-static-gray-islow")
add_test(djpeg-static-gray-islow-565-cmp "md5/md5cmp" "12f78118e56a2f48b966f792fedf23cc" "testout_gray_islow_565.bmp")
set_tests_properties(djpeg-static-gray-islow-565-cmp PROPERTIES  DEPENDS "djpeg-static-gray-islow-565")
add_test(djpeg-static-gray-islow-565D "djpeg-static" "-dct" "int" "-rgb565" "-bmp" "-outfile" "testout_gray_islow_565D.bmp" "testout_gray_islow.jpg")
set_tests_properties(djpeg-static-gray-islow-565D PROPERTIES  DEPENDS "cjpeg-static-gray-islow")
add_test(djpeg-static-gray-islow-565D-cmp "md5/md5cmp" "bdbbd616441a24354c98553df5dc82db" "testout_gray_islow_565D.bmp")
set_tests_properties(djpeg-static-gray-islow-565D-cmp PROPERTIES  DEPENDS "djpeg-static-gray-islow-565D")
add_test(cjpeg-static-420s-ifast-opt "cjpeg-static" "-sample" "2x2" "-smooth" "1" "-dct" "int" "-opt" "-outfile" "testout_420s_ifast_opt.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-420s-ifast-opt-cmp "md5/md5cmp" "388708217ac46273ca33086b22827ed8" "testout_420s_ifast_opt.jpg")
set_tests_properties(cjpeg-static-420s-ifast-opt-cmp PROPERTIES  DEPENDS "cjpeg-static-420s-ifast-opt")
add_test(cjpeg-static-3x2-float-prog "cjpeg-static" "-sample" "3x2" "-dct" "float" "-prog" "-outfile" "testout_3x2_float_prog.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-3x2-float-prog-cmp "md5/md5cmp" "9bca803d2042bd1eb03819e2bf92b3e5" "testout_3x2_float_prog.jpg")
set_tests_properties(cjpeg-static-3x2-float-prog-cmp PROPERTIES  DEPENDS "cjpeg-static-3x2-float-prog")
add_test(djpeg-static-3x2-float-prog "djpeg-static" "-dct" "float" "-outfile" "testout_3x2_float.ppm" "testout_3x2_float_prog.jpg")
set_tests_properties(djpeg-static-3x2-float-prog PROPERTIES  DEPENDS "cjpeg-static-3x2-float-prog")
add_test(djpeg-static-3x2-float-prog-cmp "md5/md5cmp" "f6bfab038438ed8f5522fbd33595dcdc" "testout_3x2_float.ppm")
set_tests_properties(djpeg-static-3x2-float-prog-cmp PROPERTIES  DEPENDS "djpeg-static-3x2-float-prog")
add_test(cjpeg-static-3x2-ifast-prog "cjpeg-static" "-sample" "3x2" "-dct" "fast" "-prog" "-outfile" "testout_3x2_ifast_prog.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-3x2-ifast-prog-cmp "md5/md5cmp" "1ee5d2c1a77f2da495f993c8c7cceca5" "testout_3x2_ifast_prog.jpg")
set_tests_properties(cjpeg-static-3x2-ifast-prog-cmp PROPERTIES  DEPENDS "cjpeg-static-3x2-ifast-prog")
add_test(djpeg-static-3x2-ifast-prog "djpeg-static" "-dct" "fast" "-outfile" "testout_3x2_ifast.ppm" "testout_3x2_ifast_prog.jpg")
set_tests_properties(djpeg-static-3x2-ifast-prog PROPERTIES  DEPENDS "cjpeg-static-3x2-ifast-prog")
add_test(djpeg-static-3x2-ifast-prog-cmp "md5/md5cmp" "fd283664b3b49127984af0a7f118fccd" "testout_3x2_ifast.ppm")
set_tests_properties(djpeg-static-3x2-ifast-prog-cmp PROPERTIES  DEPENDS "djpeg-static-3x2-ifast-prog")
add_test(cjpeg-static-420-islow-ari "cjpeg-static" "-dct" "int" "-arithmetic" "-outfile" "testout_420_islow_ari.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-420-islow-ari-cmp "md5/md5cmp" "e986fb0a637a8d833d96e8a6d6d84ea1" "testout_420_islow_ari.jpg")
set_tests_properties(cjpeg-static-420-islow-ari-cmp PROPERTIES  DEPENDS "cjpeg-static-420-islow-ari")
add_test(jpegtran-static-420-islow-ari "jpegtran-static" "-arithmetic" "-outfile" "testout_420_islow_ari2.jpg" "testimages/testimgint.jpg")
add_test(jpegtran-static-420-islow-ari-cmp "md5/md5cmp" "e986fb0a637a8d833d96e8a6d6d84ea1" "testout_420_islow_ari2.jpg")
set_tests_properties(jpegtran-static-420-islow-ari-cmp PROPERTIES  DEPENDS "jpegtran-static-420-islow-ari")
add_test(cjpeg-static-444-islow-progari "cjpeg-static" "-sample" "1x1" "-dct" "int" "-prog" "-arithmetic" "-outfile" "testout_444_islow_progari.jpg" "testimages/testorig.ppm")
add_test(cjpeg-static-444-islow-progari-cmp "md5/md5cmp" "0a8f1c8f66e113c3cf635df0a475a617" "testout_444_islow_progari.jpg")
set_tests_properties(cjpeg-static-444-islow-progari-cmp PROPERTIES  DEPENDS "cjpeg-static-444-islow-progari")
add_test(djpeg-static-420m-ifast-ari "djpeg-static" "-fast" "-ppm" "-outfile" "testout_420m_ifast_ari.ppm" "testimages/testimgari.jpg")
add_test(djpeg-static-420m-ifast-ari-cmp "md5/md5cmp" "72b59a99bcf1de24c5b27d151bde2437" "testout_420m_ifast_ari.ppm")
set_tests_properties(djpeg-static-420m-ifast-ari-cmp PROPERTIES  DEPENDS "djpeg-static-420m-ifast-ari")
add_test(jpegtran-static-420-islow "jpegtran-static" "-outfile" "testout_420_islow.jpg" "testimages/testimgari.jpg")
add_test(jpegtran-static-420-islow-cmp "md5/md5cmp" "9a68f56bc76e466aa7e52f415d0f4a5f" "testout_420_islow.jpg")
set_tests_properties(jpegtran-static-420-islow-cmp PROPERTIES  DEPENDS "jpegtran-static-420-islow")
add_test(djpeg-static-420m-islow-2_1 "djpeg-static" "-dct" "int" "-scale" "2/1" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_2_1.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-2_1-cmp "md5/md5cmp" "9f9de8c0612f8d06869b960b05abf9c9" "testout_420m_islow_2_1.ppm")
set_tests_properties(djpeg-static-420m-islow-2_1-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-2_1")
add_test(djpeg-static-420m-islow-15_8 "djpeg-static" "-dct" "int" "-scale" "15/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_15_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-15_8-cmp "md5/md5cmp" "b6875bc070720b899566cc06459b63b7" "testout_420m_islow_15_8.ppm")
set_tests_properties(djpeg-static-420m-islow-15_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-15_8")
add_test(djpeg-static-420m-islow-13_8 "djpeg-static" "-dct" "int" "-scale" "13/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_13_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-13_8-cmp "md5/md5cmp" "bc3452573c8152f6ae552939ee19f82f" "testout_420m_islow_13_8.ppm")
set_tests_properties(djpeg-static-420m-islow-13_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-13_8")
add_test(djpeg-static-420m-islow-11_8 "djpeg-static" "-dct" "int" "-scale" "11/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_11_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-11_8-cmp "md5/md5cmp" "d8cc73c0aaacd4556569b59437ba00a5" "testout_420m_islow_11_8.ppm")
set_tests_properties(djpeg-static-420m-islow-11_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-11_8")
add_test(djpeg-static-420m-islow-9_8 "djpeg-static" "-dct" "int" "-scale" "9/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_9_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-9_8-cmp "md5/md5cmp" "d25e61bc7eac0002f5b393aa223747b6" "testout_420m_islow_9_8.ppm")
set_tests_properties(djpeg-static-420m-islow-9_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-9_8")
add_test(djpeg-static-420m-islow-7_8 "djpeg-static" "-dct" "int" "-scale" "7/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_7_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-7_8-cmp "md5/md5cmp" "ddb564b7c74a09494016d6cd7502a946" "testout_420m_islow_7_8.ppm")
set_tests_properties(djpeg-static-420m-islow-7_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-7_8")
add_test(djpeg-static-420m-islow-3_4 "djpeg-static" "-dct" "int" "-scale" "3/4" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_3_4.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-3_4-cmp "md5/md5cmp" "8ed8e68808c3fbc4ea764fc9d2968646" "testout_420m_islow_3_4.ppm")
set_tests_properties(djpeg-static-420m-islow-3_4-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-3_4")
add_test(djpeg-static-420m-islow-5_8 "djpeg-static" "-dct" "int" "-scale" "5/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_5_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-5_8-cmp "md5/md5cmp" "a3363274999da2366a024efae6d16c9b" "testout_420m_islow_5_8.ppm")
set_tests_properties(djpeg-static-420m-islow-5_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-5_8")
add_test(djpeg-static-420m-islow-1_2 "djpeg-static" "-dct" "int" "-scale" "1/2" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_1_2.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-1_2-cmp "md5/md5cmp" "e692a315cea26b988c8e8b29a5dbcd81" "testout_420m_islow_1_2.ppm")
set_tests_properties(djpeg-static-420m-islow-1_2-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-1_2")
add_test(djpeg-static-420m-islow-3_8 "djpeg-static" "-dct" "int" "-scale" "3/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_3_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-3_8-cmp "md5/md5cmp" "79eca9175652ced755155c90e785a996" "testout_420m_islow_3_8.ppm")
set_tests_properties(djpeg-static-420m-islow-3_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-3_8")
add_test(djpeg-static-420m-islow-1_4 "djpeg-static" "-dct" "int" "-scale" "1/4" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_1_4.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-1_4-cmp "md5/md5cmp" "79cd778f8bf1a117690052cacdd54eca" "testout_420m_islow_1_4.ppm")
set_tests_properties(djpeg-static-420m-islow-1_4-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-1_4")
add_test(djpeg-static-420m-islow-1_8 "djpeg-static" "-dct" "int" "-scale" "1/8" "-nosmooth" "-ppm" "-outfile" "testout_420m_islow_1_8.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-1_8-cmp "md5/md5cmp" "391b3d4aca640c8567d6f8745eb2142f" "testout_420m_islow_1_8.ppm")
set_tests_properties(djpeg-static-420m-islow-1_8-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-1_8")
add_test(djpeg-static-420-islow-256 "djpeg-static" "-dct" "int" "-colors" "256" "-bmp" "-outfile" "testout_420_islow_256.bmp" "testimages/testorig.jpg")
add_test(djpeg-static-420-islow-256-cmp "md5/md5cmp" "4980185e3776e89bd931736e1cddeee6" "testout_420_islow_256.bmp")
set_tests_properties(djpeg-static-420-islow-256-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-256")
add_test(djpeg-static-420-islow-565 "djpeg-static" "-dct" "int" "-rgb565" "-dither" "none" "-bmp" "-outfile" "testout_420_islow_565.bmp" "testimages/testorig.jpg")
add_test(djpeg-static-420-islow-565-cmp "md5/md5cmp" "bf9d13e16c4923b92e1faa604d7922cb" "testout_420_islow_565.bmp")
set_tests_properties(djpeg-static-420-islow-565-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-565")
add_test(djpeg-static-420-islow-565D "djpeg-static" "-dct" "int" "-rgb565" "-bmp" "-outfile" "testout_420_islow_565D.bmp" "testimages/testorig.jpg")
add_test(djpeg-static-420-islow-565D-cmp "md5/md5cmp" "6bde71526acc44bcff76f696df8638d2" "testout_420_islow_565D.bmp")
set_tests_properties(djpeg-static-420-islow-565D-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-565D")
add_test(djpeg-static-420m-islow-565 "djpeg-static" "-dct" "int" "-nosmooth" "-rgb565" "-dither" "none" "-bmp" "-outfile" "testout_420m_islow_565.bmp" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-565-cmp "md5/md5cmp" "8dc0185245353cfa32ad97027342216f" "testout_420m_islow_565.bmp")
set_tests_properties(djpeg-static-420m-islow-565-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-565")
add_test(djpeg-static-420m-islow-565D "djpeg-static" "-dct" "int" "-nosmooth" "-rgb565" "-bmp" "-outfile" "testout_420m_islow_565D.bmp" "testimages/testorig.jpg")
add_test(djpeg-static-420m-islow-565D-cmp "md5/md5cmp" "ce034037d212bc403330df6f915c161b" "testout_420m_islow_565D.bmp")
set_tests_properties(djpeg-static-420m-islow-565D-cmp PROPERTIES  DEPENDS "djpeg-static-420m-islow-565D")
add_test(djpeg-static-420-islow-skip15_31 "djpeg-static" "-dct" "int" "-skip" "15,31" "-ppm" "-outfile" "testout_420_islow_skip15,31.ppm" "testimages/testorig.jpg")
add_test(djpeg-static-420-islow-skip15_31-cmp "md5/md5cmp" "c4c65c1e43d7275cd50328a61e6534f0" "testout_420_islow_skip15,31.ppm")
set_tests_properties(djpeg-static-420-islow-skip15_31-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-skip15_31")
add_test(djpeg-static-420-islow-ari-skip16_139 "djpeg-static" "-dct" "int" "-skip" "16,139" "-ppm" "-outfile" "testout_420_islow_ari_skip16,139.ppm" "testimages/testimgari.jpg")
add_test(djpeg-static-420-islow-ari-skip16_139-cmp "md5/md5cmp" "087c6b123db16ac00cb88c5b590bb74a" "testout_420_islow_ari_skip16,139.ppm")
set_tests_properties(djpeg-static-420-islow-ari-skip16_139-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-ari-skip16_139")
add_test(cjpeg-static-420-islow-prog "cjpeg-static" "-dct" "int" "-prog" "-outfile" "testout_420_islow_prog.jpg" "testimages/testorig.ppm")
add_test(djpeg-static-420-islow-prog-crop62x62_71_71 "djpeg-static" "-dct" "int" "-crop" "62x62+71+71" "-ppm" "-outfile" "testout_420_islow_prog_crop62x62,71,71.ppm" "testout_420_islow_prog.jpg")
set_tests_properties(djpeg-static-420-islow-prog-crop62x62_71_71 PROPERTIES  DEPENDS "cjpeg-static-420-islow-prog")
add_test(djpeg-static-420-islow-prog-crop62x62_71_71-cmp "md5/md5cmp" "26eb36ccc7d1f0cb80cdabb0ac8b5d99" "testout_420_islow_prog_crop62x62,71,71.ppm")
set_tests_properties(djpeg-static-420-islow-prog-crop62x62_71_71-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-prog-crop62x62_71_71")
add_test(djpeg-static-420-islow-ari-crop53x53_4_4 "djpeg-static" "-dct" "int" "-crop" "53x53+4+4" "-ppm" "-outfile" "testout_420_islow_ari_crop53x53,4,4.ppm" "testimages/testimgari.jpg")
add_test(djpeg-static-420-islow-ari-crop53x53_4_4-cmp "md5/md5cmp" "886c6775af22370257122f8b16207e6d" "testout_420_islow_ari_crop53x53,4,4.ppm")
set_tests_properties(djpeg-static-420-islow-ari-crop53x53_4_4-cmp PROPERTIES  DEPENDS "djpeg-static-420-islow-ari-crop53x53_4_4")
add_test(cjpeg-static-444-islow "cjpeg-static" "-dct" "int" "-sample" "1x1" "-outfile" "testout_444_islow.jpg" "testimages/testorig.ppm")
add_test(djpeg-static-444-islow-skip1_6 "djpeg-static" "-dct" "int" "-skip" "1,6" "-ppm" "-outfile" "testout_444_islow_skip1,6.ppm" "testout_444_islow.jpg")
set_tests_properties(djpeg-static-444-islow-skip1_6 PROPERTIES  DEPENDS "cjpeg-static-444-islow")
add_test(djpeg-static-444-islow-skip1_6-cmp "md5/md5cmp" "5606f86874cf26b8fcee1117a0a436a6" "testout_444_islow_skip1,6.ppm")
set_tests_properties(djpeg-static-444-islow-skip1_6-cmp PROPERTIES  DEPENDS "djpeg-static-444-islow-skip1_6")
add_test(cjpeg-static-444-islow-prog "cjpeg-static" "-dct" "int" "-prog" "-sample" "1x1" "-outfile" "testout_444_islow_prog.jpg" "testimages/testorig.ppm")
add_test(djpeg-static-444-islow-prog-crop98x98_13_13 "djpeg-static" "-dct" "int" "-crop" "98x98+13+13" "-ppm" "-outfile" "testout_444_islow_prog_crop98x98,13,13.ppm" "testout_444_islow_prog.jpg")
set_tests_properties(djpeg-static-444-islow-prog-crop98x98_13_13 PROPERTIES  DEPENDS "cjpeg-static-444-islow-prog")
add_test(djpeg-static-444-islow-prog-crop98x98_13_13-cmp "md5/md5cmp" "db87dc7ce26bcdc7a6b56239ce2b9d6c" "testout_444_islow_prog_crop98x98,13,13.ppm")
set_tests_properties(djpeg-static-444-islow-prog-crop98x98_13_13-cmp PROPERTIES  DEPENDS "djpeg-static-444-islow-prog-crop98x98_13_13")
add_test(cjpeg-static-444-islow-ari "cjpeg-static" "-dct" "int" "-arithmetic" "-sample" "1x1" "-outfile" "testout_444_islow_ari.jpg" "testimages/testorig.ppm")
add_test(djpeg-static-444-islow-ari-crop37x37_0_0 "djpeg-static" "-dct" "int" "-crop" "37x37+0+0" "-ppm" "-outfile" "testout_444_islow_ari_crop37x37,0,0.ppm" "testout_444_islow_ari.jpg")
set_tests_properties(djpeg-static-444-islow-ari-crop37x37_0_0 PROPERTIES  DEPENDS "cjpeg-static-444-islow-ari")
add_test(djpeg-static-444-islow-ari-crop37x37_0_0-cmp "md5/md5cmp" "cb57b32bd6d03e35432362f7bf184b6d" "testout_444_islow_ari_crop37x37,0,0.ppm")
set_tests_properties(djpeg-static-444-islow-ari-crop37x37_0_0-cmp PROPERTIES  DEPENDS "djpeg-static-444-islow-ari-crop37x37_0_0")
add_test(jpegtran-static-crop "jpegtran-static" "-crop" "120x90+20+50" "-transpose" "-perfect" "-outfile" "testout_crop.jpg" "testimages/testorig.jpg")
add_test(jpegtran-static-crop-cmp "md5/md5cmp" "b4197f377e621c4e9b1d20471432610d" "testout_crop.jpg")
set_tests_properties(jpegtran-static-crop-cmp PROPERTIES  DEPENDS "jpegtran-static-crop")
subdirs("simd")
subdirs("md5")
