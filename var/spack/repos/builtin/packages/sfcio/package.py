# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sfcio(CMakePackage):
    """The SFCIO library provides an API to read the NCEP Spectral model surface
    files.

    This is part of the NCEPLIBS project."""

    homepage = "https://noaa-emc.github.io/NCEPLIBS-sfcio"
    url      = "https://github.com/NOAA-EMC/NCEPLIBS-sfcio/archive/refs/tags/v1.4.1.tar.gz"

    maintainers = ['t-brown', 'kgerheiser', 'Hang-Lei-NOAA', 'edwardhartnett']

    version('1.4.1', sha256='d9f900cf18ec1a839b4128c069b1336317ffc682086283443354896746b89c59')

    def setup_run_environment(self, env):
        lib = find_libraries('libsfcio', root=self.prefix, shared=False, recursive=True)
        # Only one library version, but still need to set _4 to make NCO happy
        for suffix in ('4', ''):
            env.set('SFCIO_LIB' + suffix, lib[0])
            env.set('SFCIO_INC' + suffix, join_path(self.prefix, 'include'))
