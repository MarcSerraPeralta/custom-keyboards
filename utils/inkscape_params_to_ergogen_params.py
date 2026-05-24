import numpy as np


def get_s_params(
    w: float, h: float, a_col1: float, a_col2: float
) -> tuple[float, float, float]:
    """
    Returns the "s parameters" (splay, spread, stagger) for the
    given width and height (w,h) that separates the centers of the
    bottom keys in two consecutive columns and the angles of these
    two columns.

    Parameters
    ----------
    w
        Horizontal separation of the centers of the bottom keys in
        each column. "Horizontal" means with the standard orientation
        of the cartesian axes.
    h
        Vertical separation of the centers of the bottom keys in
        each column. "Vertical" means with the standard orientation
        of the cartesian axes.
    a_col1
        Angle (in degrees) of the first column with respect to the standard oriented
        cartesian axes. The angle starts from the standard X axis and goes to the
        bottom line of the column. A counterclockwise rotation has positive sign.
    a_col2
        Angle (in degrees) of the second column with respect to the standard oriented
        cartesian axes. The angle starts from the standard X axis and goes to the
        bottom line of the column. A counterclockwise rotation has positive sign.

    Returns
    -------
    splay
        Splay parameter (in degrees) for Ergogen.
    spread
        Spread parameter for Ergogen.
    stagger
        Stagger parameter for Ergogen.
    """
    splay = a_col2 - a_col1

    angle = a_col1 * np.pi / 180
    rot_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )
    rot_e1 = rot_matrix @ np.array([1, 0])
    rot_e2 = rot_matrix @ np.array([0, 1])

    vector = np.array([w, h])
    spread = (vector * rot_e1).sum()
    stagger = (vector * rot_e2).sum()

    return splay, float(spread), float(stagger)
