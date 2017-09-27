#Table Creation for value exporting in the database:

CREATE TABLE "RestData"
(
  sampler integer,
  clump_thickness integer,
  cell_size integer,
  cell_shape integer,
  adhesion integer,
  epithelial_cell_size integer,
  nuclei_chromatin integer,
 chromatin integer, normal_nucleoli integer,
  mitoses_class integer,
  class integer)WITH (
  OIDS=FALSE
);