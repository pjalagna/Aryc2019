head="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
  <!--Created by yEd 3.20-->
  <key attr.name="Description" attr.type="string" for="graph" id="d0"/>
  <key for="port" id="d1" yfiles.type="portgraphics"/>
  <key for="port" id="d2" yfiles.type="portgeometry"/>
  <key for="port" id="d3" yfiles.type="portuserdata"/>
  <key attr.name="url" attr.type="string" for="node" id="d4"/>
  <key attr.name="description" attr.type="string" for="node" id="d5"/>
  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="graphml" id="d7" yfiles.type="resources"/>
  <key attr.name="url" attr.type="string" for="edge" id="d8"/>
  <key attr.name="description" attr.type="string" for="edge" id="d9"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>
  <graph edgedefault="directed" id="G">
    <data key="d0"/>
    <node id="n0">
      <data key="d5"/>
      <data key="d6">
        <y:ShapeNode>
          <y:Geometry height="84.0" width="261.0" x="52.0" y="23.0"/>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" raised="false" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="88.796875" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="219.220703125" x="20.8896484375" xml:space="preserve" y="-2.3984375">template 
7/18/2020
PJA
test1 - OK
test2 - generate from mock relate -OK
test2a - 2 mock relate - OK
test3 - generate from real relate -
--need to layout to fix positions<y:LabelModel><y:SmartNodeLabelModel distance="4.0"/></y:LabelModel><y:ModelParameter><y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/></y:ModelParameter></y:NodeLabel>
          <y:Shape type="rectangle"/>
        </y:ShapeNode>
      </data>
    </node>
"""
#refidT "%refidNode%" %refid%
refidT = """    <node id="%refidNode%">
      <data key="d5"/>
      <data key="d6">
        <y:GenericNode configuration="com.yworks.flowchart.terminator">
          <y:Geometry height="40.0" width="80.0" x="142.5" y="182.0"/>
          <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="31.029296875" x="24.4853515625" xml:space="preserve" y="10.93359375">%refid%<y:LabelModel><y:SmartNodeLabelModel distance="4.0"/></y:LabelModel><y:ModelParameter><y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/></y:ModelParameter></y:NodeLabel>
        </y:GenericNode>
      </data>
    </node>
"""
#centerT "%cent%" 
centerT = """    <node id="%cent%">
      <data key="d5"/>
      <data key="d6">
        <y:GenericNode configuration="com.yworks.flowchart.start2">
          <y:Geometry height="12.0" width="31.0" x="167.0" y="269.0"/>
          <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" hasText="false" height="4.0" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="4.0" x="13.5" y="4.0">
            <y:LabelModel>
              <y:SmartNodeLabelModel distance="4.0"/>
            </y:LabelModel>
            <y:ModelParameter>
              <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/>
            </y:ModelParameter>
          </y:NodeLabel>
        </y:GenericNode>
      </data>
    </node>
"""
v1v2T = """
    <node id="%v1v2Node%">
      <data key="d5"/>
      <data key="d6">
        <y:GenericNode configuration="com.yworks.entityRelationship.big_entity">
          <y:Geometry height="90.0" width="80.0" x="20.0" y="230.0"/>
          <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" backgroundColor="#B7C9E3" configuration="com.yworks.entityRelationship.label.name" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="internal" modelPosition="t" textColor="#000000" verticalTextPosition="bottom" visible="true" width="19.43359375" x="30.283203125" xml:space="preserve" y="4.0">%v1%</y:NodeLabel>
          <y:NodeLabel alignment="left" autoSizePolicy="content" configuration="com.yworks.entityRelationship.label.attributes" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="top" visible="true" width="19.43359375" x="2.0" xml:space="preserve" y="30.1328125">%v2%<y:LabelModel><y:ErdAttributesNodeLabelModel/></y:LabelModel><y:ModelParameter><y:ErdAttributesNodeLabelModelParameter/></y:ModelParameter></y:NodeLabel>
          <y:StyleProperties>
            <y:Property class="java.lang.Boolean" name="y.view.ShadowNodePainter.SHADOW_PAINTING" value="true"/>
          </y:StyleProperties>
        </y:GenericNode>
      </data>
    </node>
"""
v5v6 = """
    <node id="%v5v6Node%">
      <data key="d5"/>
      <data key="d6">
        <y:GenericNode configuration="com.yworks.entityRelationship.big_entity">
          <y:Geometry height="90.0" width="80.0" x="286.86287934553275" y="230.0"/>
          <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" backgroundColor="#B7C9E3" configuration="com.yworks.entityRelationship.label.name" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="internal" modelPosition="t" textColor="#000000" verticalTextPosition="bottom" visible="true" width="19.43359375" x="30.283203125" xml:space="preserve" y="4.0">%v5%</y:NodeLabel>
          <y:NodeLabel alignment="left" autoSizePolicy="content" configuration="com.yworks.entityRelationship.label.attributes" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="top" visible="true" width="19.43359375" x="2.0" xml:space="preserve" y="30.1328125">%v6%<y:LabelModel><y:ErdAttributesNodeLabelModel/></y:LabelModel><y:ModelParameter><y:ErdAttributesNodeLabelModelParameter/></y:ModelParameter></y:NodeLabel>
          <y:StyleProperties>
            <y:Property class="java.lang.Boolean" name="y.view.ShadowNodePainter.SHADOW_PAINTING" value="true"/>
          </y:StyleProperties>
        </y:GenericNode>
      </data>
    </node>
"""
# predicateT "%predNode%" "%v3%" "%v4%"
predicateT = """    <node id="%predNode%">
      <data key="d5"/>
      <data key="d6">
        <y:GenericNode configuration="com.yworks.flowchart.document">
          <y:Geometry height="40.0" width="80.0" x="150.0" y="373.0"/>
          <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="46.78515625" x="16.607421875" xml:space="preserve" y="10.93359375">%v3% :: %v4%<y:LabelModel><y:SmartNodeLabelModel distance="4.0"/></y:LabelModel><y:ModelParameter><y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/></y:ModelParameter></y:NodeLabel>
        </y:GenericNode>
      </data>
    </node>
"""
#edgeT "%edg%" "%srcNode%" "%objNode%" "%text%"
edgeT = """     <edge id="%edg%" source="%srcNode%" target="%objNode%">
      <data key="d10">
        <y:PolyLineEdge>
          <y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
          <y:EdgeLabel alignment="center" configuration="AutoFlippingLabel" distance="2.0" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="custom" preferredPlacement="anywhere" ratio="0.5" textColor="#000000" verticalTextPosition="bottom" visible="true" width="59.751953125" x="45.0732421875" xml:space="preserve" y="23.96915128839322">"%text%"<y:LabelModel><y:SmartEdgeLabelModel autoRotationEnabled="false" defaultAngle="0.0" defaultDistance="10.0"/></y:LabelModel><y:ModelParameter><y:SmartEdgeLabelModelParameter angle="0.0" distance="30.0" distanceToCenter="true" position="right" ratio="0.5" segment="0"/></y:ModelParameter><y:PreferredPlacementDescriptor angle="0.0" angleOffsetOnRightSide="0" angleReference="absolute" angleRotationOnRightSide="co" distance="-1.0" frozen="true" placement="anywhere" side="anywhere" sideReference="relative_to_edge_flow"/></y:EdgeLabel>
          <y:BendStyle smoothed="false"/>
        </y:PolyLineEdge>
      </data>
    </edge>
    """

tailT = """  </graph>
  <data key="d7">
    <y:Resources/>
  </data>
</graphml>
"""
Nv1v2T = """
    <node id="%Node%">
      <data key="d5"/>
      <data key="d6">
        <y:GenericNode configuration="com.yworks.entityRelationship.big_entity">
          <y:Geometry height="90.0" width="80.0" x="20.0" y="230.0"/>
          <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" backgroundColor="#B7C9E3" configuration="com.yworks.entityRelationship.label.name" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="internal" modelPosition="t" textColor="#000000" verticalTextPosition="bottom" visible="true" width="19.43359375" x="30.283203125" xml:space="preserve" y="4.0">%v1%</y:NodeLabel>
          <y:NodeLabel alignment="left" autoSizePolicy="content" configuration="com.yworks.entityRelationship.label.attributes" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.1328125" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="top" visible="true" width="19.43359375" x="2.0" xml:space="preserve" y="30.1328125">%v2%<y:LabelModel><y:ErdAttributesNodeLabelModel/></y:LabelModel><y:ModelParameter><y:ErdAttributesNodeLabelModelParameter/></y:ModelParameter></y:NodeLabel>
          <y:StyleProperties>
            <y:Property class="java.lang.Boolean" name="y.view.ShadowNodePainter.SHADOW_PAINTING" value="true"/>
          </y:StyleProperties>
        </y:GenericNode>
      </data>
    </node>
"""