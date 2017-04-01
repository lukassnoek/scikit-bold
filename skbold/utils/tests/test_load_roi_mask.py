import pytest
from ..roi_globals import available_atlases, other_rois
from ...utils import load_roi_mask, parse_roi_labels


@pytest.mark.parametrize("atlas_name", available_atlases)
@pytest.mark.parametrize("resolution", ['2mm'])  # Testing 1mm takes too long
@pytest.mark.parametrize("lateralized", [False, True])
@pytest.mark.parametrize("threshold", [0, 25])
# @pytest.mark.parametrize("maxprob", [True, False])  # TAKES VERY LONG
def test_load_roi_mask_from_atlas(atlas_name, resolution, lateralized,
                                  threshold):
    maxprob = False  # Hardcoded to test
    info_dict = parse_roi_labels(atlas_type=atlas_name,
                                 lateralized=lateralized)
    rois = info_dict.keys()

    for roi in rois:
        mask = load_roi_mask(roi, atlas_name=atlas_name, resolution=resolution,
                             lateralized=lateralized, which_hemifield='left',
                             threshold=threshold, maxprob=maxprob)
        assert(mask.ndim == 3)
        assert(mask.sum() > 0)


@pytest.mark.parametrize("roi_name", other_rois)
@pytest.mark.parametrize("threshold", [0, 25])
def test_load_roi_mask_from_other_rois(roi_name, threshold):

    mask = load_roi_mask(roi_name, threshold=threshold)
