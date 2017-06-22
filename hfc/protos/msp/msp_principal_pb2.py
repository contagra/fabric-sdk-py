# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/msp/msp_principal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/msp/msp_principal.proto',
  package='common',
  syntax='proto3',
  serialized_pb=_b('\n\"hfc/protos/msp/msp_principal.proto\x12\x06\x63ommon\"\xa9\x01\n\x0cMSPPrincipal\x12\x45\n\x18principal_classification\x18\x01 \x01(\x0e\x32#.common.MSPPrincipal.Classification\x12\x11\n\tprincipal\x18\x02 \x01(\x0c\"?\n\x0e\x43lassification\x12\x08\n\x04ROLE\x10\x00\x12\x15\n\x11ORGANIZATION_UNIT\x10\x01\x12\x0c\n\x08IDENTITY\x10\x02\"q\n\x10OrganizationUnit\x12\x16\n\x0emsp_identifier\x18\x01 \x01(\t\x12&\n\x1eorganizational_unit_identifier\x18\x02 \x01(\t\x12\x1d\n\x15\x63\x65rtifiers_identifier\x18\x03 \x01(\x0c\"r\n\x07MSPRole\x12\x16\n\x0emsp_identifier\x18\x01 \x01(\t\x12)\n\x04role\x18\x02 \x01(\x0e\x32\x1b.common.MSPRole.MSPRoleType\"$\n\x0bMSPRoleType\x12\n\n\x06MEMBER\x10\x00\x12\t\n\x05\x41\x44MIN\x10\x01\x42P\n$org.hyperledger.fabric.protos.commonZ(github.com/hyperledger/fabric/protos/mspb\x06proto3')
)



_MSPPRINCIPAL_CLASSIFICATION = _descriptor.EnumDescriptor(
  name='Classification',
  full_name='common.MSPPrincipal.Classification',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORGANIZATION_UNIT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDENTITY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=153,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_MSPPRINCIPAL_CLASSIFICATION)

_MSPROLE_MSPROLETYPE = _descriptor.EnumDescriptor(
  name='MSPRoleType',
  full_name='common.MSPRole.MSPRoleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MEMBER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADMIN', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=411,
  serialized_end=447,
)
_sym_db.RegisterEnumDescriptor(_MSPROLE_MSPROLETYPE)


_MSPPRINCIPAL = _descriptor.Descriptor(
  name='MSPPrincipal',
  full_name='common.MSPPrincipal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal_classification', full_name='common.MSPPrincipal.principal_classification', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='principal', full_name='common.MSPPrincipal.principal', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSPPRINCIPAL_CLASSIFICATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=216,
)


_ORGANIZATIONUNIT = _descriptor.Descriptor(
  name='OrganizationUnit',
  full_name='common.OrganizationUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msp_identifier', full_name='common.OrganizationUnit.msp_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='organizational_unit_identifier', full_name='common.OrganizationUnit.organizational_unit_identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='certifiers_identifier', full_name='common.OrganizationUnit.certifiers_identifier', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=331,
)


_MSPROLE = _descriptor.Descriptor(
  name='MSPRole',
  full_name='common.MSPRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msp_identifier', full_name='common.MSPRole.msp_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='common.MSPRole.role', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSPROLE_MSPROLETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=447,
)

_MSPPRINCIPAL.fields_by_name['principal_classification'].enum_type = _MSPPRINCIPAL_CLASSIFICATION
_MSPPRINCIPAL_CLASSIFICATION.containing_type = _MSPPRINCIPAL
_MSPROLE.fields_by_name['role'].enum_type = _MSPROLE_MSPROLETYPE
_MSPROLE_MSPROLETYPE.containing_type = _MSPROLE
DESCRIPTOR.message_types_by_name['MSPPrincipal'] = _MSPPRINCIPAL
DESCRIPTOR.message_types_by_name['OrganizationUnit'] = _ORGANIZATIONUNIT
DESCRIPTOR.message_types_by_name['MSPRole'] = _MSPROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MSPPrincipal = _reflection.GeneratedProtocolMessageType('MSPPrincipal', (_message.Message,), dict(
  DESCRIPTOR = _MSPPRINCIPAL,
  __module__ = 'hfc.protos.msp.msp_principal_pb2'
  # @@protoc_insertion_point(class_scope:common.MSPPrincipal)
  ))
_sym_db.RegisterMessage(MSPPrincipal)

OrganizationUnit = _reflection.GeneratedProtocolMessageType('OrganizationUnit', (_message.Message,), dict(
  DESCRIPTOR = _ORGANIZATIONUNIT,
  __module__ = 'hfc.protos.msp.msp_principal_pb2'
  # @@protoc_insertion_point(class_scope:common.OrganizationUnit)
  ))
_sym_db.RegisterMessage(OrganizationUnit)

MSPRole = _reflection.GeneratedProtocolMessageType('MSPRole', (_message.Message,), dict(
  DESCRIPTOR = _MSPROLE,
  __module__ = 'hfc.protos.msp.msp_principal_pb2'
  # @@protoc_insertion_point(class_scope:common.MSPRole)
  ))
_sym_db.RegisterMessage(MSPRole)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$org.hyperledger.fabric.protos.commonZ(github.com/hyperledger/fabric/protos/msp'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
