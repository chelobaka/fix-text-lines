"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import inkex

class FixMultilineText(inkex.Effect):

  def effect(self):
    role = inkex.addNS('role', 'sodipodi')
    svg = self.document.getroot()
    for element in svg.iter(inkex.addNS('tspan', 'svg')):
      element.set(role, 'line')

if __name__ == '__main__':
    e = FixMultilineText()
    e.affect()
