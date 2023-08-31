import sublime, sublime_plugin
import os
import datetime
import random
import getpass

''' Add license stamp
/**
* @version   $Id: ${1:current_file_name.extension} ${2:random_4_digit_number} ${3:YYYY-MM-DD} ${4:time_in_UTC_24} ${5:current_logged-in_user} $
* @author    Company http://example.com
* @copyright Copyright (C) 2007 - ${6:current_year} Company
* @license   http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 only
*/
'''

class AddLicenseStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        file_name = os.path.basename(file_path)
        year = datetime.datetime.utcnow().strftime("%Y")

        license = """/*
 * {} - <brief description>
 *
 * Copyright (C) {} [github.com/nickelulz]
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */""".format(file_name, year)

        self.view.replace(edit, self.view.sel()[0], license)
