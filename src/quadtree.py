from __future__ import annotations
import os
import tkinter as tk


class QuadTree:
    """
    Represents a quadtree data structure for hierarchical decomposition of 2D space.

    Attributes:
        NB_NODES (int): The number of child nodes in each quadtree node, which is always 4.

    Methods:
        __init__(self, hg, hd, bd, bg): Initialize a QuadTree node with its four child nodes
        depth(self) -> int: Calculate and return the recursion depth of the quadtree
        from_file(filename: str) -> QuadTree: Create a QuadTree from a textual file
        from_list(data: list) -> QuadTree: Create a QuadTree from a list representation

    Example:
        To create a QuadTree instance:
        >>> my_quadtree = QuadTree(hg, hd, bd, bg)
    Usage:
        - You can use the 'depth' property to determine the depth of the quadtree.
        - The 'from_file' and 'from_list' static methods are used for creating quadtree
          instances from file or list representations.
    """

    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg  # Sous-arbre en haut à gauche
        self.hd = hd  # Sous-arbre en haut à droite
        self.bd = bd  # Sous-arbre en bas à droite
        self.bg = bg  # Sous-arbre en bas à gauche

    @property
    def depth(self) -> int:
        """
        Calculate and return the recursion depth of the quadtree.

        This method calculates the depth of the quadtree by recursively traversing the tree structure and determining
        the maximum depth from the root node to the deepest leaf node.

        Returns:
            int: The depth of the quadtree, which is the maximum number of levels in the tree.
        """
        depths = [0]
        if isinstance(self.hg, QuadTree):
            depths.append(self.hg.depth)
        if isinstance(self.hd, QuadTree):
            depths.append(self.hd.depth)
        if isinstance(self.bd, QuadTree):
            depths.append(self.bd.depth)
        if isinstance(self.bg, QuadTree):
            depths.append(self.bg.depth)
        return 1 + max(depths)

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """
        Create a QuadTree instance from a textual file.

        This static method reads the content of a given textual file containing a representation of a quadtree and
        constructs a QuadTree instance from it.

        Args:
            filename (str): The name of the file containing the quadtree representation.

        Returns:
            QuadTree: A QuadTree instance representing the quadtree structure read from the file.

        Example:
            To create a QuadTree instance from a file named 'quadtree.txt':
            >>> tree_from_file = QuadTree.from_file('quadtree.txt')

        Note:
            The file should contain a valid representation of a quadtree in a suitable format
            to be successfully parsed and converted into a QuadTree instance.
        """
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        parent_directory = os.path.abspath(os.path.join(file_path, os.pardir))
        filename = '../files/quadtree-easy.txt'
        txt_file = os.path.join(parent_directory, 'files', filename)

        with open(txt_file, 'r') as file:
            data = eval(file.read())
        return QuadTree.from_list(data)

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """
        Create a QuadTree instance from a list representation.

        This static method constructs a QuadTree instance from a nested list representation, where each element
        in the list corresponds to a node in the quadtree structure.

        Args:
            data (list): A list representation of the quadtree structure. The list should follow a valid format
            where each element can be either a nested list representing a subquad or an integer (0 or 1)
            indicating a leaf node.

        Returns:
            QuadTree: A QuadTree instance representing the quadtree structure defined by
            the provided list.

        Example:
            To create a QuadTree instance from a list representation:
            >>> quadtree_data = [[1, 0], [0, 0]]
            >>> tree_from_list = QuadTree.from_list(quadtree_data)

        Note:
            The 'data' list should adhere to the expected format with nested lists for
            subquads and integers (0 or 1) for leaf nodes to be successfully converted
            into a QuadTree instance.
        """
        if isinstance(data, list):
            if isinstance(data[0], list):
                hg, hd, bd, bg = (QuadTree.from_list(list_item) for list_item in data)
                return QuadTree(hg, hd, bd, bg)
            else:
                return QuadTree(*data)


class TkQuadTree(QuadTree):
    """
    Represents a QuadTree for graphical visualization using the Tkinter library.

    TkQuadTree is a subclass of QuadTree that specializes in visualizing the quadtree structure on a graphical
    canvas using the Tkinter library.

    Attributes:
        data: The data representing the quadtree structure for visualization.
        root: The Tkinter root window for the graphical display.
        canvas: The Tkinter canvas used for drawing the quadtree.

    Methods:
        __init__(self, data): Initialize a TkQuadTree instance with data for visualization.
        draw(self, x, y, size, node): Recursively draw the quadtree on the canvas.
        paint(self): Draw the quadtree on the canvas and display the graphical representation.

    Example:
        To create a TkQuadTree instance for visualization:
        >>> data = [[1, 0], [0, 0]]
        >>> my_tk_quadtree = TkQuadTree(data)

    Usage:
        - The `draw` method is responsible for drawing the quadtree structure on the canvas.
        - The `paint` method is used to display the graphical representation of the quadtree.
    """

    def __init__(self, data):
        super().__init__(False, False, False, False)
        self.data = data
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw(0, 0, 400, self.data)

    def draw(self, x, y, size, node):
        """
        Recursively draw the quadtree structure on the canvas.

        This method is responsible for visually representing the quadtree structure
        on the Tkinter canvas by recursively drawing nodes based on their positions
        and sizes.

        Args:
            x (int): The x-coordinate of the top-left corner of the current node's bounding box.
            y (int): The y-coordinate of the top-left corner of the current node's bounding box.
            size (int): The size of the current node's bounding box.
            node: The current node to be drawn. It can be a list representing subquads or
                  an integer (0 or 1) indicating a leaf node.

        Example:
            To draw a quadtree structure on the canvas, you can call this method, specifying
            the initial coordinates (x, y) and the size of the root node's bounding box.

            >>> data = [[1, 0], [0, 0]]
            >>> my_tk_quadtree = TkQuadTree(data)
            >>> my_tk_quadtree.draw(0, 0, 400, data)

        Note:
            This method is typically called recursively to draw the entire quadtree structure.
            It handles both leaf nodes (0 or 1) and subquads (represented as nested lists).
            You can customize the drawing appearance within this method if needed.
        """

        if isinstance(node, list):
            half_size = size // 2
            self.draw(x, y, half_size, node[0])
            self.draw(x + half_size, y, half_size, node[1])
            self.draw(x, y + half_size, half_size, node[2])
            self.draw(x + half_size, y + half_size, half_size, node[3])
        elif isinstance(node, int):
            fill_color = 'lightgrey' if node == 0 else 'black'
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=fill_color, outline='black')

    def paint(self):
        """
        Draw the quadtree on the canvas and display the graphical representation.

        This method is responsible for drawing the entire quadtree structure on the
        Tkinter canvas, and then displaying the graphical representation in a Tkinter
        window.

        Example:
        To create and display a graphical representation of the quadtree:
        >>> data = [[1, 0], [0, 0]]
        >>> my_tk_quadtree = TkQuadTree(data)
        >>> my_tk_quadtree.paint()

        Note:
        After calling this method, a graphical window will be displayed with the
        visual representation of the quadtree. You can customize the appearance of
        the canvas and the window within this method if needed.
        """
        # Draw an empty rectangle or leaf
        self.root.mainloop()


def main():
    """
    Main function for running the TkQuadTree visualization.

    This function serves as the entry point for running the TkQuadTree visualization.
    It reads data from a file, creates a TkQuadTree instance, and displays the graphical
    representation of the quadtree.

    Example:
    To execute the quadtree visualization:
    >>> main()

    Note:
    This function reads data from a file, so ensure that the file 'quadtree.txt'
    or the specified file path exists and contains a valid representation of a quadtree
    structure in the expected format.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    parent_directory = os.path.abspath(os.path.join(file_path, os.pardir))
    filename = '../files/quadtree.txt'
    txt_file = os.path.join(parent_directory, 'files', filename)
    with open(txt_file, 'r') as file:
        data = eval(file.read())

    tk_quadtree = TkQuadTree(data)
    tk_quadtree.paint()


if __name__ == "__main__":
    main()
